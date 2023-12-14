import cv2
import numpy as np

from src.graphic.camera import Camera
from src.graphic.scene import Scene
from src.geometry.vector import Vector
from src.geometry.triangularMesh import TriangularMesh
from src.utils.loaders import Loaders
from src.geometry.transformation import Transformation  # Importa a classe Transformation

def main():
    # Carregar vértices e triângulos do arquivo OBJ
    vertices, triangles = Loaders.importObjFile('src/assets/humanoid.obj')

    # Imprimir os vértices antes da transformação
    # print("Vértices antes da transformação:")
    # for vertex in vertices:
    #     print(vertex)  # Isso imprimirá cada objeto Vector antes da transformação

    # Aplicar transformação de rotação de 180 graus no eixo X
    vertices = Transformation.rotate_180_x(vertices)

    # Imprimir os vértices depois da transformação
    # print("\nVértices depois da transformação:")
    # for vertex in vertices:
    #     print(vertex)  # Isso imprimirá cada objeto Vector depois da transformação

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

    # Criar a cena e adicionar a malha
    scene = Scene()
    scene.addMesh(mesh)

    # Configurar a câmera e gerar a imagem
    camera = Camera(location, focus, v_up, distance, width, height)
    matrix = camera.take(scene)

    # Converter a matriz de cores para uma imagem OpenCV
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            color = matrix[y][x]
            img[y][x] = [int(color.r), int(color.g), int(color.b)]

    # Exibir a imagem antes da transformação
    cv2.imshow('Render Antes', img)
    cv2.waitKey(0)

    # Aplicar transformação na imagem (rotação 180 graus)
    img_transformed = cv2.flip(img, -1)

    # Exibir a imagem depois da transformação
    cv2.imshow('Render Depois', img_transformed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
