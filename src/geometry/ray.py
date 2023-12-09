from src.geometry.vector import Vector

class Ray():
    def __init__(self, point: Vector, direction: Vector):
        self.point = point
        self.direction = direction.normalize()
        