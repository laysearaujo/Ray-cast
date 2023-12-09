import cv2
import numpy as np

from src.graphic.camera import Camera
from src.graphic.scene import Scene
from src.geometry.vector import Vector
from src.geometry.triangularMesh import TriangularMesh

# from src.data.FirstDeliveryTestData import spheres, planes
from src.data.SecondDeliveryTestData import spheres, planes, vertices, triangles

def main():
    width, height = 800, 600
    v_up = Vector(0, 1, 0)

    # Ajustando os parâmetros da câmera
    location = Vector(0, 0, 150)
    focus = Vector(0, 0, 0)
    distance = 100

    # Criando a malha triangular e adicionando triângulos a ela
    mesh = TriangularMesh(vertices, triangles)

    # Criação da cena
    scene = Scene()

    # Adição de esferas, planos e triângulos à cena
    for sphere in spheres:
        scene.addSphere(sphere)
    for plane in planes:
        scene.addPlane(plane)
    
    # Adição da máscara
    scene.addMesh(mesh)

    # Configuração da câmera e geração da imagem
    camera = Camera(location, focus, v_up, distance, width, height)
    matrix = camera.take(scene)

    # Conversão da matriz de cores para uma imagem OpenCV
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
