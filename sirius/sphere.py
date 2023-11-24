from .vector import Vector
from .color import Color
from .ray import Ray
import math

class Sphere:
    def __init__(self, center: Vector, radius: float, color: Color):
        self.center = center
        self.radius = radius
        self.color = color

    def normalAt(self, point: Vector):
        normal_vector = point.sub(self.center)
        return normal_vector.normalize()

    def intersectRay(self, ray: Ray):
        oc = ray.point.sub(self.center)

        a = ray.direction.dot(ray.direction)
        b = 2.0 * oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius * self.radius

        delta = b * b - 4 * a * c

        # Se delta negativo
        if delta < 0:
            return {
                "color": None,
                "distance": None,
                "normal": None
            }

        # Calcula as duas soluções da equação quadrática
        t = (-b - math.sqrt(delta)) / (2 * a)

        return {
                "color": self.color,
                "distance": t,
                # "normal": self.normalAt()
            }