from ..entity.triangle import Triangle
from .vector import Vector

class TriangularMesh:
    def __init__(self, vertices: list, triangles: list, normals: list):
        self.vertices = vertices
        self.triangles = [Triangle(vertices[i], vertices[j], vertices[k]) for i, j, k in triangles]
        self.normals = normals

    def intersect(self, ray):
        # Lógica de interseção com o raio
        pass

    def addTriangle(self, triangle: Triangle):
        self.triangles.append(triangle)
