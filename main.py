import cv2
import numpy as np

from src.entity.sphere import Sphere
from src.entity.plane import Plane
from src.geometry.vector import Vector
from src.graphic.color import Color
from src.graphic.camera import Camera
from src.graphic.scene import Scene

def main():
    width, height = 800, 600
    v_up = Vector(0, 1, 0)

    # Ajustando os parâmetros da câmera
    location = Vector(0, 0, -10) 
    focus = Vector(0, 0, 0)
    distance = 10

    spheres = [
        Sphere(Vector(-10, 0, 0), 2, Color(255, 0, 0)),     # Esfera vermelha à esquerda
        Sphere(Vector(0, 0, 0), 3, Color(0, 255, 0)),      # Esfera verde no centro
        Sphere(Vector(10, 0, 0), 4, Color(0, 0, 255))      # Esfera azul à direita
    ]

    planes = [
        Plane(Vector(0, -15, 0), Vector(0, 1, 0), Color(200, 200, 200))  # Plano abaixo das esferas
    ]

    scene = Scene()

    for sphere in spheres:
        scene.addSphere(sphere)
    
    for plane in planes:
        scene.addPlane(plane)

    camera = Camera(location, focus, v_up, distance, width, height)

    matrix = camera.take(scene)

    # Convertendo a matriz de cores para uma imagem OpenCV
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
