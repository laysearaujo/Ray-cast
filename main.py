import cv2
import numpy as np

from src.entity.sphere import Sphere
from src.entity.plane import Plane
from src.entity.triangle import Triangle
from src.graphic.color import Color
from src.graphic.camera import Camera
from src.graphic.scene import Scene
from src.geometry.vector import Vector
from src.geometry.triangularMesh import TriangularMesh

def main():
    width, height = 800, 600
    v_up = Vector(0, 1, 0)

    # Ajustando os parâmetros da câmera
    location = Vector(0, 0, -10)
    focus = Vector(0, 0, 0)
    distance = 10

    # Definição das esferas
    spheres = [
        Sphere(Vector(-10, 0, 0), 2, Color(255, 0, 0)), # Esfera vermelha
        Sphere(Vector(0, 8, 0), 3, Color(0, 255, 0)), # Esfera verde
        Sphere(Vector(10, 0, 0), 4, Color(0, 0, 255)), # Esfera azul
    ]

    # Definição dos planos
    planes = [
        Plane(Vector(0, -15, 0), Vector(0, 1, 0), Color(200, 200, 200)), # Plano cinza
    ]

    # Criando vértices e triângulos para a malha
    vertices = [
        Vector(4, 0, 2), Vector(3, 2, 2), Vector(5, 0, 2),
        Vector(-2, -5, 2), Vector(0, -1, 3), Vector(8, -1, 2), 
        Vector(-3, 4, 2), Vector(-6, 1, 2), Vector(-4, 6, 3),
        Vector(4, -1, 2), Vector(5, 2, 2), Vector(1, -1, 7),
    ]

    triangles = [
        Triangle(vertices[0], vertices[1], vertices[2], Color(128, 0, 128)), # Triângulo roxo
        Triangle(vertices[3], vertices[4], vertices[5], Color(0, 255, 255)),  # Triângulo azul
        Triangle(vertices[6], vertices[7], vertices[8], Color(255, 0, 255)),  # Triângulo rosa
        Triangle(vertices[9], vertices[10], vertices[11], Color(255, 165, 0)), # Triângulo amarelo
    ]

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
