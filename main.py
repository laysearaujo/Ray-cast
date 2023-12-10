import cv2
import numpy as np

from src.graphic.camera import Camera
from src.graphic.scene import Scene
from src.geometry.vector import Vector
from src.geometry.triangularMesh import TriangularMesh
from src.utils.loaders import Loaders

def main():
    # Carregar vértices e triângulos do arquivo OBJ
    vertices, triangles = Loaders.importObjFile('src/data/humanoid.obj')

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
    distance = 100

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

    cv2.imshow('Render', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
