from ..geometry.vector import Vector

class Triangle:
    def __init__(self, vertex1: Vector, vertex2: Vector, vertex3: Vector):
        self.vertices = [vertex1, vertex2, vertex3]

    def normal(self):
        edge1 = self.vertices[1].sub(self.vertices[0])
        edge2 = self.vertices[2].sub(self.vertices[0])
        return edge1.cross(edge2).normalize()