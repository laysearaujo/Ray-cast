from typing import List, Tuple
from src.geometry.vector import Vector
from src.entity.triangle import Triangle
from src.graphic.color import Color

class Loaders:

    @staticmethod
    def importObjFile(filename: str) -> Tuple[List[Vector], List[Triangle]]:
        vertices = []
        triangles = []

        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('v '):  # Definição de vértices
                    parts = line.split()
                    # Ignora o quarto valor (geralmente 1.0) se estiver presente
                    x, y, z = map(float, parts[1:4])
                    vertices.append(Vector(x, y, z))
                elif line.startswith('f '):  # Definição de faces (triângulos)
                    parts = line.split()
                    # Assume que cada face é um triângulo
                    vertex_indices = [int(p.split('/')[0]) - 1 for p in parts[1:4]]  # OBJ indices start at 1
                    triangle_vertices = [vertices[i] for i in vertex_indices]
                    triangles.append(Triangle(*triangle_vertices, color=Color(255, 255, 255)))  # Cor padrão

        return vertices, triangles

