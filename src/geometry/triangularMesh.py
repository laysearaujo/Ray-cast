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

    def addVertex(self, vertice: Vector):
        self.vertices.append(vertice)

    def addTriangle(self, triangle: Triangle):
        self.triangles.append(triangle)
        self.normals.append(triangle.normal())

    def __eq__(self, other):
        if len(self.vertices) != len(other.vertices) or len(self.triangles) != len(other.triangles):
            return False
        
        for i in range(len(self.vertices)):
            if self.vertices[i] != other.vertices[i]:
                return False
        
        for i in range(len(self.triangles)):
            if self.triangles[i] != other.triangles[i]:
                return False
        
        return True