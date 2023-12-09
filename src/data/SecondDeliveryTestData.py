from src.entity.triangle import Triangle
from src.graphic.color import Color
from src.geometry.vector import Vector

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