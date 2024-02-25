import cv2
import math
import numpy as np

from src.graphic.camera import Camera
from src.graphic.scene import Scene
from src.geometry.vector import Vector
from src.geometry.triangularMesh import TriangularMesh
from src.entity.triangle import Triangle
from src.utils.loaders import Loaders
from src.entity.sphere import Sphere
from src.entity.plane import Plane
from src.graphic.color import Color
from src.graphic.light import Light
from src.graphic.material import Material

def main():
    width, height = 800, 600
    v_up = Vector(0, 1, 0)

    # Ajustando os parâmetros da câmera para melhor visualização
    location = Vector(0, 0, -25)  # Posição da câmera mais recuada
    focus = Vector(0, 0, 0)       # Alterando a direção do foco para o centro da cena
    distance = 70                 # Reduzindo a distância da câmera

    # 0.5, // kd
    # 0.9, // ks
    # 0.1, // ka
    # 0.1, // kr
    # 0.1, // kt
    # 1.0 // roughness
    material = Material(
        Color(125, 125, 125),
        Color(200, 200, 200),
        Color(25, 25, 25),
        Color(25, 25, 25),
        Color(25, 25, 25),
        1
    )

    spheres = [
        Sphere(Vector(-10, 0, 0), 5, Color(255, 0, 0), material),     # Esfera vermelha à esquerda
        Sphere(Vector(0, 0, 0), 5, Color(0, 255, 0), material),      # Esfera verde no centro
        Sphere(Vector(10, 0, 0), 5, Color(0, 0, 255), material)      # Esfera azul à direita
    ]

    planes = [
        Plane(Vector(0, -15, 0), Vector(0, 1, 0), Color(200, 200, 200), material)  # Plano abaixo das esferas
    ]

    scene = Scene()

    light = Light(Vector(0, 10, 7), Color(255, 255, 255))
    scene.addLight(light)

    for sphere in spheres:
        scene.addSphere(sphere)
    
    for plane in planes:
        scene.addPlane(plane)

    camera = Camera(location, focus, v_up, distance, width, height)

    # # Teste de intersecção de raio
    # ray = Ray(Vector(0,0,0), Vector(1,1,0))
    # instersect1_color, instersect1_distance, _ = spheres[0].intersect(ray).values()

    matrix = camera.take(scene)

    # Convertendo a matriz de cores para uma imagem OpenCV
    img = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            color = matrix[y][x]
            img[y][x] = [int(color.r), int(color.g), int(color.b)]

    # Exibir a imagem usando OpenCV
    cv2.imshow('Render', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
