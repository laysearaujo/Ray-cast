import math

from src.geometry.vector import Vector
from src.geometry.ray import Ray
from src.graphic.color import Color
from src.graphic.material import Material

class Sphere:
    def __init__(self, center: Vector, radius: float, color: Color, material: Material):
        self.center = center
        self.radius = radius
        self.color = color
        self.material = material

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
        
        # Calcula as soluções da equação quadrática
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
    
    def bounds(self):
        # Retorna os limites (bounds) da esfera
        min_bound = self.center.sub(Vector(self.radius, self.radius, self.radius))
        max_bound = self.center.add(Vector(self.radius, self.radius, self.radius))
        return min_bound, max_bound

    def intersect_bounds(self, bounds):
        # Determina se a esfera intersecta com os limites do nó do octree
        min_bound, max_bound = bounds
        sphere_min, sphere_max = self.bounds()

        # Verificar interseção em cada dimensão (x, y, z)
        intersects_x = sphere_max.x >= min_bound.x and sphere_min.x <= max_bound.x
        intersects_y = sphere_max.y >= min_bound.y and sphere_min.y <= max_bound.y
        intersects_z = sphere_max.z >= min_bound.z and sphere_min.z <= max_bound.z

        # Se houver interseção em todas as dimensões, a esfera intersecta os limites do nó do octree
        return intersects_x and intersects_y and intersects_z
