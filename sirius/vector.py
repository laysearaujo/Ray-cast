import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def norm(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def normalize(self):
        norm = self.norm()
        self.x /= norm
        self.y /= norm
        self.z /= norm

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