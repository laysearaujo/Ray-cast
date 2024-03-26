import cv2
import math
import numpy as np

from src.graphic.camera import Camera
from src.graphic.scene import Scene
from src.geometry.vector import Vector
from src.geometry.triangularMesh import TriangularMesh
from src.entity.sphere import Sphere
from src.entity.plane import Plane
from src.graphic.color import Color
from src.graphic.light import Light
from src.graphic.material import Material
from src.geometry.octree import Octree
from src.geometry.bezierSurface import BezierSurface
from src.entity.triangle import Triangle

def main():
    width, height = 1000, 600
    v_up = Vector(0, 1, 0)

    # Ajustando os parâmetros da câmera para melhor visualização
    location = Vector(10, 0, -10)  # Posição da câmera mais recuada
    focus = Vector(0, 0, 0)       # Alterando a direção do foco para o centro da cena
    distance = 70                 # Reduzindo a distância da câmera

    material = Material(
        Color(125, 125, 125),
        Color(200, 200, 200),
        Color(25, 25, 25),
        Color(25, 25, 25),
        Color(25, 25, 25),
        1,
        1
    )

    material1 = Material(
        Color(125, 125, 125),
        Color(200, 200, 200),
        Color(25, 25, 25),
        Color(25, 25, 25),
        Color(25, 25, 25),
        1,
        1
    )

    material2 = Material(
        Color(10, 10, 10),
        Color(10, 10, 10),
        Color(10, 10, 10),
        Color(10, 10, 10),
        Color(190, 190, 190),
        200,
        2
    )

    spheres = [
        Sphere(Vector(-10, 0, 0), 5, Color(255, 0, 0), material),     # Esfera vermelha à esquerda
        Sphere(Vector(0, 0, 0), 5, Color(0, 255, 0), material1),      # Esfera verde no centro
        Sphere(Vector(10, 0, 0), 5, Color(255, 255, 255), material2)      # Esfera azul à direita
    ]

    planes = [
        Plane(Vector(0, -15, 0), Vector(0, 1, 0), Color(255, 255, 255), material)  # Plano abaixo das esferas
    ]

    meshs = []

    control_points = np.array([
        [[-2, 2, 0], [0, 2, 0], [2, 2, 0]],
        [[-2, 0, 0], [0, 0, 4], [2, 0, 0]],
        [[-2, -2, 0], [0, -2, 0], [2, -2, 0]]
    ])  

    bazier = BezierSurface(control_points, 3, 3)

    vertices, triangles = bazier.build(material, Color(255, 255, 255), -4, 0, 0, 2)

    meshs.append(TriangularMesh(vertices, triangles, material))
  
    control_points2 = np.array([[[-0.5, -2, 0], [1, 1, 1], [2, 2, 2]],
                           [[2, 1, 0], [2, 0, -1], [2, 1, 1]],
                           [[1, -1, 2], [0, 0.5, 2], [0.5, 1, 2]]])

    bazier2 = BezierSurface(control_points2, 3, 3)

    vertices, triangles = bazier2.build(material, Color(255, 255, 255), -3, 0, 10, 2)

    meshs.append(TriangularMesh(vertices, triangles, material))

    scene = Scene()

    light = Light(Vector(1, 64, 10), Color(255, 255, 255))
    scene.addLight(light)
    light = Light(Vector(49, 20, 3), Color(255, 255, 255))
    scene.addLight(light)

    for sphere in spheres:
        scene.addSphere(sphere)
    
    for plane in planes:
        scene.addPlane(plane)
    
    for mesh in meshs:
        scene.addMesh(mesh)

    octree = Octree()
    octree.build(meshs)  # Construir o octree com esferas e planos

    scene.setOctree(octree)

    camera = Camera(location, focus, v_up, distance, width, height)

    # Tirar a cena usando a câmera e o octree
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
