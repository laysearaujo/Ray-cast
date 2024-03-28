import numpy as np
from src.entity.triangle import Triangle
from src.graphic.color import Color
from src.geometry.vector import Vector

class BezierSurface:

    def __init__(self, control_points, u_cells=100, w_cells=100):
        self.control_points = control_points
        self.u_cells = u_cells
        self.w_cells = w_cells
        self.x_bezier = None 
        self.y_bezier = None
        self.z_bezier = None

    def build(self, material, color: Color, x_offset=0, y_offset=0, z_offset=0, scale=1):
        u_pts = np.size(self.control_points[0], 0)
        w_pts = np.size(self.control_points[0], 1)
        n = u_pts - 1
        m = w_pts - 1

        u = np.linspace(0, 1, self.u_cells)
        w = np.linspace(0, 1, self.w_cells)

        self.x_bezier = np.zeros((self.u_cells, self.w_cells))
        self.y_bezier = np.zeros((self.u_cells, self.w_cells))
        self.z_bezier = np.zeros((self.u_cells, self.w_cells))

        for i in range(0, u_pts):
            for j in range(0, w_pts):
                Jt = self.J(n, i, u).transpose()

                self.x_bezier += np.dot(Jt, self.K(m, j, w)) * self.control_points[0, i, j]
                self.y_bezier += np.dot(Jt, self.K(m, j, w)) * self.control_points[1, i, j]
                self.z_bezier += np.dot(Jt, self.K(m, j, w)) * self.control_points[2, i, j]

        self.x_bezier *= scale   
        self.y_bezier *= scale
        self.z_bezier *= scale

        self.x_bezier += x_offset
        self.y_bezier += y_offset
        self.z_bezier += z_offset

        vertices_cv, triangles_cv = [], []

        for i in range(self.u_cells - 1):
            for j in range(self.w_cells - 1):
                v1 = Vector(self.x_bezier[i, j], self.y_bezier[i, j], self.z_bezier[i, j])
                v2 = Vector(self.x_bezier[i+1, j], self.y_bezier[i+1, j], self.z_bezier[i+1, j])
                v3 = Vector(self.x_bezier[i, j+1], self.y_bezier[i, j+1], self.z_bezier[i, j+1])

                vertices_cv.extend([v1, v2, v3])
                triangles_cv.append(Triangle(v1, v2, v3, Color(0, 255, 0), material=material))

                v1 = Vector(self.x_bezier[i+1, j], self.y_bezier[i+1, j], self.z_bezier[i+1, j])
                v2 = Vector(self.x_bezier[i+1, j+1], self.y_bezier[i+1, j+1], self.z_bezier[i+1, j+1])
                v3 = Vector(self.x_bezier[i, j+1], self.y_bezier[i, j+1], self.z_bezier[i, j+1])

                vertices_cv.extend([v1, v2, v3])
                triangles_cv.append(Triangle(v1, v2, v3, Color(0, 255, 0), material=material))

        return vertices_cv, triangles_cv

    def Ni(self, n, i):
        return np.math.factorial(n) / (np.math.factorial(i) * np.math.factorial(n - i))

    def Mj(self, m, j):
        return np.math.factorial(m) / (np.math.factorial(j) * np.math.factorial(m - j))

    def J(self, n, i, u):
        return np.matrix(self.Ni(n, i) * (u ** i) * (1 - u) ** (n - i))

    def K(self, m, j, w):
        return np.matrix(self.Mj(m, j) * (w ** j) * (1 - w) ** (m - j))

    def rotate_y(self, points, angle):
        rotation_matrix = np.array([
            [np.cos(angle), 0, np.sin(angle)],
            [0, 1, 0],
            [-np.sin(angle), 0, np.cos(angle)]
        ])
        return np.dot(points, rotation_matrix.T)