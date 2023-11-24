from .vector import Vector
from .color import Color

class Plane:
    def __init__(self, point: Vector, normal: Vector, color: Color):
        self.point = point
        self.normal = normal
        self.color = color