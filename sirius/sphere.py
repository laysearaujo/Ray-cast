from .vector import Vector
from .color import Color
from .ray import Ray

class Sphere:
    def __init__(self, center: Vector, radius: float, color: Color):
        self.center = center
        self.radius = radius
        self.color = color

    def intersectRay(ray: Ray):
        return ray