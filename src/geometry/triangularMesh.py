from typing import List

from src.entity.triangle import Triangle
from src.geometry.vector import Vector
from src.geometry.ray import Ray

class TriangularMesh:
    def __init__(self, vertices: List[Vector], triangles: List[Triangle], material):
        self.vertices = vertices
        self.triangles = triangles
        self.normals = [triangle.normal() for triangle in triangles]
        self.material = material

    def intersect(self, ray: Ray):
        closest_intersection = {
            "distance": float('inf'),
            "color": None,
            "normal": None
        }
        for triangle in self.triangles:
            intersection = triangle.intersect(ray)
            if intersection and intersection["distance"] < closest_intersection["distance"]:
                closest_intersection = intersection
        return closest_intersection

    def addVertex(self, vertice: Vector):
        self.vertices.append(vertice)

    def addTriangle(self, triangle: Triangle):
        self.triangles.append(triangle)
        self.normals.append(triangle.normal())

    # def __eq__(self, other):
    #     if len(self.vertices) != len(other.vertices) or len(self.triangles) != len(other.triangles):
    #         return False
        
    #     for i in range(len(self.vertices)):
    #         if self.vertices[i] != other.vertices[i]:
    #             return False
        
    #     for i in range(len(self.triangles)):
    #         if self.triangles[i] != other.triangles[i]:
    #             return False
        
    #     return True

    def bounds(self):
        # Inicializa os limites com os valores extremos para min e max
        min_bound = Vector(float('inf'), float('inf'), float('inf'))
        max_bound = Vector(float('-inf'), float('-inf'), float('-inf'))

        # Encontra os limites da malha triangular
        for vertex in self.vertices:
            min_bound = min_bound.min(vertex)
            max_bound = max_bound.max(vertex)

        return min_bound, max_bound

    def intersect_bounds(self, bounds):
        # Verifica se os limites da malha intersectam com os limites do nó do octree
        min_bound, max_bound = bounds
        mesh_min, mesh_max = self.bounds()

        # Verifica se há interseção em cada dimensão (x, y, z)
        intersects_x = mesh_max.x >= min_bound.x and mesh_min.x <= max_bound.x
        intersects_y = mesh_max.y >= min_bound.y and mesh_min.y <= max_bound.y
        intersects_z = mesh_max.z >= min_bound.z and mesh_min.z <= max_bound.z

        # Retorna True se houver interseção em todas as dimensões, caso contrário, False
        return intersects_x and intersects_y and intersects_z
