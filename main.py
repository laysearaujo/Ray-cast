from src.geometry.vector import Vector
from src.entity.triangle import Triangle
from src.geometry.ray import Ray

# Criar triângulos de teste
vertex1 = Vector(0, 0, 0)
vertex2 = Vector(1, 0, 0)
vertex3 = Vector(0, 1, 0)
normal = Vector(0, 0, 1)
triangle = Triangle(vertex1, vertex2, vertex3, normal)

# Criar um raio de teste
ray_origin = Vector(0.1, 0.1, -1)
ray_direction = Vector(0, 0, 1)
ray = Ray(ray_origin, ray_direction)

# Testar a interseção entre o raio e o triângulo
intersection = triangle.intersect(ray)

if intersection:
    print("Interseção encontrada!")
    print(type(intersection))
    for key in intersection:
        print(f"{key}: {intersection[key]}")
else:
    print("Nenhuma interseção encontrada.")

if intersection:
    print("Interseção encontrada!")
    print("Vetor Normal:", intersection["normal"])
    print("Cor:", intersection["color"])
    print("Distância ao longo do raio:", intersection["t"])
else:
    print("Nenhuma interseção encontrada.")