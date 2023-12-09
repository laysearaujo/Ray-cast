from ..geometry.vector import Vector
from ..graphic.color import Color

class Triangle:
    def __init__(self, v0: Vector, v1: Vector, v2: Vector, color: Color):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2
        self.color = color

    def intersect(self, ray):
        edge1 = self.v1.sub(self.v0)
        edge2 = self.v2.sub(self.v0)
        h = ray.direction.cross(edge2)
        a = edge1.dot(h)

        if a > -0.00001 and a < 0.00001:
            return None  # O raio é paralelo ao triângulo

        f = 1 / a
        s = ray.point.sub(self.v0)
        u = f * s.dot(h)

        if u < 0 or u > 1:
            return None

        q = s.cross(edge1)
        v = f * ray.direction.dot(q)

        if v < 0 or u + v > 1:
            return None

        t = f * edge2.dot(q)
        if t > 0.00001:
            # intersect_point = ray.point.add(ray.direction.multByScalar(t))
            normal = self.calculateNormal()
            return {
                "normal": normal,
                "t": t,
                "color": self.color   
            }
        return None
    
    def calculateNormal(self):
        return self.v1.sub(self.v0).cross(self.v2.sub(self.v0)).normalize()

    def isPointInside(self, point):
        # Verificar se um ponto está dentro do triângulo usando coordenadas baricêntricas
        v0v1 = self.v1.sub(self.v0)
        v0v2 = self.v2.sub(self.v0)
        v0p = point.sub(self.v0)

        dot00 = v0v1.dot(v0v1)
        dot01 = v0v1.dot(v0v2)
        dot02 = v0v1.dot(v0p)
        dot11 = v0v2.dot(v0v2)
        dot12 = v0v2.dot(v0p)

        inv_denom = 1 / (dot00 * dot11 - dot01 * dot01)
        u = (dot11 * dot02 - dot01 * dot12) * inv_denom
        v = (dot00 * dot12 - dot01 * dot02) * inv_denom

        return (u >= 0) and (v >= 0) and (u + v < 1)
