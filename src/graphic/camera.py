import math
from ..geometry.ray import Ray

class Camera:
    def __init__(self, location, focus, v_up, distance, width, height, fov=90):
        self.location = location
        self.v_front = focus.sub(location).normalize()
        self.v_right = self.v_front.cross(v_up).normalize()
        self.v_up = self.v_right.cross(self.v_front).normalize()
        self.distance = distance
        self.width = width
        self.height = height
        self.pixel_height = 2 * distance * math.tan(math.radians(90) / 2) / height
        # new_width = self.pixel_height * self.width
        # aspect_ratio = new_width / width
        # self.pixel_width = self.pixel_height * aspect_ratio
        self.pixel_width = 2 * distance * math.tan(math.radians(90) / 2) / height
    def take(self, scene):
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
    
    def createRay(self, x, y):
        direction = self.v_front.multByScalar(self.distance)
        right_offset = self.v_right.multByScalar((x - self.width / 2) * self.pixel_width)
        up_offset = self.v_up.multByScalar((self.height / 2 - y) * self.pixel_height)
        
        total_offset = right_offset.add(up_offset)
        direction = direction.add(total_offset).normalize()
        
        return Ray(self.location, direction)
