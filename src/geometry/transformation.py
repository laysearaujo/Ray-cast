class Transformation:
    @staticmethod
    def rotate_180_x(vertices):
        for i in range(len(vertices)):
            vertices[i].x *= -1
            vertices[i].y *= -1
            vertices[i].z *= -1
        return vertices
