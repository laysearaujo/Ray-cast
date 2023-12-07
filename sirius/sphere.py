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

    def intersect(self, ray: Ray):
        oc = ray.point.sub(self.center)

        a = ray.direction.dot(ray.direction)
        b = 2.0 * oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius * self.radius

        delta = b * b - 4 * a * c

        if delta < 0:
            return {
                "color": Color(0, 0, 0),
                "distance": float('inf'),
                "normal": None
            }
        
        # Calcula soluções da equação quadrática
        t1 = (-b - math.sqrt(delta)) / (2 * a)
        t2 = (-b + math.sqrt(delta)) / (2 * a)

        if t1 < 0 and t2 < 0:
            return {
                "color": Color(0, 0, 0),
                "distance": float('inf'),
                "normal": None
            }

        intersection_point = ray.point.add(ray.direction.multByScalar(t1 if t1 >= 0 and t1 < t2 else t2))
        normal = self.normalAt(intersection_point).normalize()

        return {
            "color": self.color,
            "distance": t1 if t1 >= 0 and t1 < t2 else t2,
            "normal": normal
        }
