import math

class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f'[{self.x},{self.y},{self.z}]'
    
    def norm(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def normalize(self):
        norm = self.norm()
        self.x /= norm
        self.y /= norm
        self.z /= norm
        return self

    def sub(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def cross(self, other):
        i = (self.y * other.z) - (self.z * other.y)
        j = (self.z * other.x) - (self.x * other.z)
        k = (self.x * other.y) - (self.y * other.x)

        return Vector(i, j, k)
    
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def multByScalar(self, k):
        return Vector(self.x * k, self.y * k, self.z * k)
    
    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    
    def rotateX (self, alpha):
        ry = math.cos(alpha) * self.y - math.sin(alpha) * self.z
        rz = math.sin(alpha) * self.y + math.cos(alpha) * self.z

        return Vector(self.x, ry, rz)

    def rotateY(self, alpha):
        rx = math.cos(alpha) * self.x + math.sin(alpha) * self.z
        rz = -math.sin(alpha) * self.x + math.cos(alpha) * self.z

        return Vector(rx, self.y, rz)

    def rotateZ(self, alpha):
        rx = math.cos(alpha) * self.x - math.sin(alpha) * self.y
        ry = math.sin(alpha) * self.x + math.cos(alpha) * self.y

        return Vector(rx, ry, self.z)

    def translateX (self, num):
        
        return Vector(self.x + num, self.y, self.z)

    def translateY (self, num):
        
        return Vector(self.x, self.y + num, self.z)
    
    def translateZ (self, num):
        
        return Vector(self.x, self.y, self.z + num)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
