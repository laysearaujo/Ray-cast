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
                if line.startswith('v '):  # Definição de vertices
                    _, x, y, z = line.split()
                    vertices.append(Vector(float(x), float(y), float(z)))
                elif line.startswith('f '):  # Definição de faces (triângulos)
                    _, *vertex_indices = line.split()
                    vertex_indices = [int(index.split('/')[0]) - 1 for index in vertex_indices] 
                    triangle_vertices = [vertices[i] for i in vertex_indices]
                    triangles.append(Triangle(*triangle_vertices, color=Color(255, 255, 255)))  # Cor padrão

        return vertices, triangles
