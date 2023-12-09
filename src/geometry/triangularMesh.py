from typing import List

from src.entity.triangle import Triangle
from src.geometry.vector import Vector
from src.geometry.ray import Ray

class TriangularMesh:
    def __init__(self, vertices: List[Vector] = [], triangles: List[Triangle] = []):
        self.vertices = vertices
        self.triangles = triangles
        self.normals = [triangle.normal() for triangle in triangles]

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

    def addVertice(self, vertice: Vector):
        self.vertices.append(vertice)

    def addTriangle(self, triangle: Triangle):
        self.triangles.append(triangle)
        self.normals.append(triangle.normal())
