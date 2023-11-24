class Ray():
    def __init__(self, point, direction):
        self.point = point
        self.direction = direction.normalize()
        