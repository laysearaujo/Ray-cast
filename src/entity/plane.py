from src.geometry.vector import Vector
from src.geometry.ray import Ray
from src.graphic.color import Color
from src.graphic.material import Material

class Plane:
    def __init__(self, point: Vector, normal: Vector, color: Color, material: Material):
        self.point = point
        self.normal = normal.normalize()  # Normalizando a normal para ter certeza
        self.color = color
        self.material = material

    def intersect(self, ray: Ray):
        direction_dot_normal = ray.direction.dot(self.normal)

        # Se o raio é paralelo ao plano, não há interseção
        if abs(direction_dot_normal) < 1e-6:
            return {
                "color": Color(0, 0, 0),
                "distance": float('inf'),
                "normal": self.normal  # A normal do plano é constante
            }

        # Calcular o valor de t, que indica onde o raio intercepta o plano
        t = self.point.sub(ray.point).dot(self.normal) / direction_dot_normal

        # Verificar se a interseção está na direção positiva do raio
        if t >= 0:
            return {
                "color": self.color,
                "distance": t,
                "normal": self.normal  # A normal do plano é constante
            }
        else:
            return {
                "color": Color(0, 0, 0),
                "distance": float('inf'),
                "normal": self.normal  # Mesmo não havendo interseção válida, a normal é constante
            }

    def bounds(self):
        # Como o plano é infinito, seus limites serão um intervalo muito grande
        # Aqui, estamos definindo um cubo muito grande em torno do plano
        min_bound = Vector(float('-inf'), float('-inf'), float('-inf'))
        max_bound = Vector(float('inf'), float('inf'), float('inf'))
        return min_bound, max_bound

    def intersect_bounds(self, bounds):
        # Como o plano é infinito, ele sempre intersecta com os limites do nó do octree
        return True
