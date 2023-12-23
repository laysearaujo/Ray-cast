import cv2
import math
import numpy as np

from src.graphic.camera import Camera
from src.graphic.scene import Scene
from src.geometry.vector import Vector
from src.geometry.triangularMesh import TriangularMesh
from src.utils.loaders import Loaders

def main():
    # Carregar vértices e triângulos do arquivo OBJ
    vertices, triangles = Loaders.importObjFile('src/assets/humanoid.obj')

    triangles_rotated = []

    # Aplicar transformação de rotação de 90 graus no eixo X
    rotated_vertices = [vertex.rotateY(math.pi / 2) for vertex in vertices]

    for triangle in triangles:
        triangle_rotated_vertices = [vertex.rotateY(math.pi / 2) for vertex in triangle.vertices]
        triangles_rotated.append(
            Triangle(triangle_rotated_vertices[0], 
            triangle_rotated_vertices[1], 
            triangle_rotated_vertices[2], 
            triangle.color ))
            
    # Ajustar o tamanho da janela
    width, height = 400, 300
    v_up = Vector(0, 1, 0)

    # Calcular o centro dos vértices para posicionar a câmera
    center = Vector(0, 0, 0)
    for vertex in vertices:
        center = center.add(vertex)
    center = center.multByScalar(1 / len(vertices))

    # Ajustar a posição e a distância da câmera para enquadrar o modelo
    location = Vector(center.x, center.y, center.z + 50)
    focus = center
    distance = 10

    # Criar a malha triangular e adicionar os triângulos a ela
    mesh = TriangularMesh(vertices, triangles)
    mesh_rotated = TriangularMesh(rotated_vertices, triangles_rotated)

    for i, vertex in enumerate(mesh.vertices):
        mesh_rotated.vertices[i] = vertex.rotateY(math.pi / 2)

    # Criar a cena e adicionar as malhas
    scene = Scene()
    scene.addMesh(mesh)
    scene_rotated = Scene()
    scene_rotated.addMesh(mesh_rotated)

    # Configurar a câmera e gerar as imagens para ambas as cenas
    camera = Camera(location, focus, v_up, distance, width, height)
    matrix = camera.take(scene)
    matrix_rotated = camera.take(scene_rotated)

    # Converter as matrizes de cores para imagens OpenCV (original e rotacionada)
    img = np.zeros((height, width, 3), dtype=np.uint8)
    img_transformed = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            color = matrix[y][x]
            img[y][x] = [int(color.r), int(color.g), int(color.b)]

            color_rotated = matrix_rotated[y][x]
            img_transformed[y][x] = [int(color_rotated.r), int(color_rotated.g), int(color_rotated.b)]

           # print(img == img_transformed)

    # Criar a imagem combinada (original e rotacionada)
    combined_img = np.zeros((height, 2 * width, 3), dtype=np.uint8)
    combined_img[:height, :width, :] = img
    combined_img[:height, width:2 * width, :] = img_transformed

    # Exibir as duas imagens lado a lado
    cv2.imshow('Imagem Original vs. Rotacionada', combined_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
