from src.entity.sphere import Sphere
from src.entity.plane import Plane
from src.graphic.color import Color
from src.geometry.vector import Vector

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