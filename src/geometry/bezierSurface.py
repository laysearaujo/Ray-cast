import numpy as np
import matplotlib.pyplot as pyplot
import math
import cv2
from src.entity.triangle import Triangle
from src.graphic.color import Color
from src.geometry.vector import Vector



class BezierSurface:

    def __init__(self, control_points, uCELLS=100, wCELLS=100):
        self.control_points = control_points
        self.uCELLS = uCELLS
        self.wCELLS = wCELLS
        self.xBezier = None 
        self.yBezier = None
        self.zBezier = None


    def build(self, material, color: Color, xOffset=0, yOffset=0, zOffset=0, scalle = 1):

        uPTS = np.size(self.control_points[0], 0)
        wPTS = np.size(self.control_points[0], 1)

        n = uPTS - 1
        m = wPTS - 1

        u = np.linspace(0, 1, self.uCELLS)
        w = np.linspace(0, 1, self.wCELLS)

        self.xBezier = np.zeros((self.uCELLS, self.wCELLS))
        self.yBezier = np.zeros((self.uCELLS, self.wCELLS))
        self.zBezier = np.zeros((self.uCELLS, self.wCELLS))

        for i in range(0, uPTS):
            for j in range(0, wPTS):
                Jt = self.J(n, i, u).transpose()

                self.xBezier = Jt * self.K(m, j, w) * self.control_points[0, i, j] +  self.xBezier
                self.yBezier = Jt * self.K(m, j, w) * self.control_points[1, i, j] +  self.yBezier
                self.zBezier = Jt * self.K(m, j, w) * self.control_points[2, i, j] +  self.zBezier

        triangles = []
        trianglesCV = []
        verticesCV = []

        self.xBezier *= scalle   
        self.yBezier *= scalle
        self.zBezier *= scalle

        self.xBezier = self.xBezier + xOffset
        self.yBezier = self.yBezier + yOffset
        self.zBezier = self.zBezier + zOffset

        for i in range(self.uCELLS - 1):
            for j in range(self.wCELLS - 1):

                vector1 = Vector(self.xBezier[i, j], self.yBezier[i, j], self.zBezier[i, j])
                vector2 = Vector(self.xBezier[i+1, j], self.yBezier[i+1, j], self.zBezier[i+1, j])
                vector3 = Vector(self.xBezier[i, j+1], self.yBezier[i, j+1], self.zBezier[i, j+1])

                verticesCV.append(vector1)
                verticesCV.append(vector2)
                verticesCV.append(vector3)

                trianglesCV.append(Triangle(vector1, vector2, vector3, Color(0, 255, 0), material=material))

                vector1 = Vector(self.xBezier[i+1, j], self.yBezier[i+1, j], self.zBezier[i+1, j])
                vector2 = Vector(self.xBezier[i+1, j+1], self.yBezier[i+1, j+1], self.zBezier[i+1, j+1])
                vector3 = Vector(self.xBezier[i, j+1], self.yBezier[i, j+1], self.zBezier[i, j+1])

                verticesCV.append(vector1)
                verticesCV.append(vector2)
                verticesCV.append(vector3)

                trianglesCV.append(Triangle(vector1, vector2, vector3, Color(0, 255, 0), material=material))

        return verticesCV, trianglesCV


    def plot():

        for i in range(self.uCELLS - 1):
            for j in range(self.wCELLS - 1):
        
                # Coordenadas dos vértices do triângulo
                v0 = [self.xBezier[i, j], self.yBezier[i, j], self.zBezier[i, j]]
                v1 = [self.xBezier[i+1, j], self.yBezier[i+1, j], self.zBezier[i+1, j]]
                v2 = [self.xBezier[i, j+1], self.yBezier[i, j+1], self.zBezier[i, j+1]]
                
                # Adiciona os vértices do triângulo à lista de triângulos
                triangles.append([v0, v1, v2])

                # Coordenadas dos vértices do segundo triângulo
                v0 = [self.xBezier[i+1, j], self.yBezier[i+1, j], zBezier[i+1, j]]
                v1 = [self.xBezier[i+1, j+1], self.yBezier[i+1, j+1], zBezier[i+1, j+1]]
                v2 = [self.xBezier[i, j+1], self.yBezier[i, j+1], self.zBezier[i, j+1]]
                
                # Adiciona os vértices do segundo triângulo à lista de triângulos
                triangles.append([v0, v1, v2])

        # Cria a figura e os eixos 3D
        fig = pyplot.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plota os triângulos
        for triangle in triangles:
            triangle = np.array(triangle)
            ax.plot_trisurf(triangle[:, 0], triangle[:, 1], triangle[:, 2], color='blue')

        # Configura os rótulos dos eixos
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Mostra o gráfico
        pyplot.show() 

    def Ni(self, n, i):
        return math.factorial(n) / (math.factorial(i) * math.factorial(n - i))

    def Mj(self, m, j):
        return math.factorial(m) / (math.factorial(j) * math.factorial(m - j))

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


