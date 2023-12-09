import os

from src.entity.triangle import Triangle
from src.graphic.color import Color
from src.geometry.vector import Vector
from src.utils.loaders import Loaders

'''
# Criando vértices, triângulos, esferas e planos para a malha
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
'''

spheres = [] 

planes = []


# Criando vértices e triângulos a partir de arquivo .obj
current_file_dir = os.path.dirname(os.path.abspath(__file__))
obj_filename = os.path.join(current_file_dir, "diamond.obj")
vertices, triangles = Loaders.importObjFile(obj_filename)