import cv2
import numpy as np

from src.graphic.camera import Camera
from src.graphic.scene import Scene
from src.geometry.vector import Vector
from src.graphic.color import Color
from src.graphic.light import Light
from src.graphic.material import Material
from src.geometry.bezierSurface import BezierSurface
from src.geometry.triangularMesh import TriangularMesh
from src.geometry.octree import Octree

def main():
    # Configurações da janela de renderização
    width, height = 1000, 600

    # Configurações da câmera
    camera_location = Vector(0, 0, -20)  # Posição da câmera ajustada para dentro da curva
    camera_focus = Vector(0, 0, 0)
    camera_up = Vector(0, -1, 0)
    camera_distance = 10

    # Girar a câmera em torno do eixo Z em 5 graus
    rotation_angle = 4.5  # Graus
    camera_location = camera_location.rotateX(rotation_angle)
    camera_focus = camera_focus.rotateZ(rotation_angle)
    camera_up = camera_up.rotateZ(0)

    # Configurações dos materiais
    material1 = Material(
        Color(125, 125, 125),  # Ambient
        Color(200, 200, 200),  # Diffuse
        Color(25, 25, 25),     # Specular
        Color(25, 25, 25),     # Reflection
        Color(25, 25, 25),     # Refraction
        1,                     # Shininess
        1                      # Transparency
    )

    # Criação da superfície de Bézier
    control_points = np.array([
        [[-2, 2, 0], [0, 2, 0], [2, 2, 0]],
        [[-2, 0, 0], [0, 0, 4], [2, 0, 0]],
        [[-2, -2, 0], [0, -2, 0], [2, -2, 0]]
    ])

    bezier_surface = BezierSurface(control_points, 10, 10)
    vertices, triangles = bezier_surface.build(material1, Color(255, 255, 255), -4, 0, 0, 2)
    mesh = TriangularMesh(vertices, triangles, material1)


    # Configuração das luzes
    lights = [
        Light(Vector(1, 64, 10), Color(255, 255, 255)),
        Light(Vector(49, 20, 3), Color(255, 255, 255))
    ]

    # Criação da cena
    scene = Scene()
    scene.addMesh(mesh)
    for light in lights:
        scene.addLight(light)

    # Construção do octree
    octree = Octree()
    octree.build([mesh])
    scene.setOctree(octree)

    # Configuração e renderização da cena
    camera = Camera(camera_location, camera_focus, camera_up, camera_distance, width, height)
    matrix = camera.take(scene)

    # Conversão da matriz de cores para uma imagem OpenCV
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            color = matrix[y][x]
            img[y][x] = [int(color.r), int(color.g), int(color.b)]

    # Exibição da imagem usando OpenCV
    cv2.imshow('Render', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
