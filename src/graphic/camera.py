import math

from src.geometry.ray import Ray
from src.geometry.vector import Vector
from src.graphic.scene import Scene

class Camera:
    def __init__(self, location: Vector, focus: Vector, v_up: Vector, distance: float, width: float, height: float):
        self.location = location
        self.v_front = focus.sub(location).normalize()
        self.v_right = self.v_front.cross(v_up).normalize()
        self.v_up = self.v_right.cross(self.v_front).normalize()
        self.distance = distance
        self.width = width
        self.height = height
        self.pixel_height = 2 * distance * math.tan(math.radians(90) / 2) / height
        self.pixel_width = 2 * distance * math.tan(math.radians(90) / 2) / height

    def take(self, scene: Scene):
        matrix = []
        for y in range(self.height):
            list_aux = []
            for x in range(self.width):
                ray = self.createRay(x, y)
                intersection_info = scene.intersect(ray)
                color = intersection_info["color"]
                list_aux.append(color)
            matrix.append(list_aux)
        return matrix
    
    def createRay(self, x: float, y: float):
        direction = self.v_front.multByScalar(self.distance)
        right_offset = self.v_right.multByScalar((x - self.width / 2) * self.pixel_width)
        up_offset = self.v_up.multByScalar((self.height / 2 - y) * self.pixel_height)
        
        total_offset = right_offset.add(up_offset)
        direction = direction.add(total_offset).normalize()
        
        return Ray(self.location, direction)
