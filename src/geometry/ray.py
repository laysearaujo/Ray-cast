from src.geometry.vector import Vector

class Ray():
    def __init__(self, point: Vector, direction: Vector):
        self.point = point
        self.direction = direction.normalize()
    
    def pointAt(self, distance):
        return Vector(self.direction.x * distance + self.point.x,
                      self.direction.y * distance + self.point.y,
                      self.direction.z * distance + self.point.z)