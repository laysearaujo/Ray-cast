import cv2
import numpy as np

from sirius.sphere import Sphere
from sirius.plane import Plane
from sirius.vector import Vector
from sirius.color import Color
from sirius.camera import Camera
from sirius.scene import Scene
from sirius.ray import Ray

def main():
    width, height = 800, 600
    v_up = Vector(0, 1, 0)

    # Ajustando os parâmetros da câmera para melhor visualização
    location = Vector(0, 0, -10)  # Posição da câmera mais recuada
    focus = Vector(0, 0, 0)       # Alterando a direção do foco para o centro da cena
    distance = 40                 # Reduzindo a distância da câmera

    spheres = [
        Sphere(Vector(-10, 0, 0), 5, Color(255, 0, 0)),     # Esfera vermelha à esquerda
        Sphere(Vector(0, 0, 0), 5, Color(0, 255, 0)),      # Esfera verde no centro
        Sphere(Vector(10, 0, 0), 5, Color(0, 0, 255))      # Esfera azul à direita
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
