from src.geometry.vector import Vector
from src.graphic.color import Color

class Surface:
    def __init__(self, point: Vector, normal: Vector, color: Color, distance: int):
        self.point = point
        self.normal = normal
        self.color = color
        self.distance = distance
    
    def getReflection(self, direction: Vector):
        tNormal = self.normal.normalize()
        tDirection = direction.normalize()

        return tNormal.multByScalar(2.0 * tNormal.dot(tDirection)).sub(tDirection).normalize()
