from src.geometry.vector import Vector
from src.geometry.ray import Ray
from src.graphic.color import Color
from src.graphic.material import Material

class Triangle:
    def __init__(self, vertex1: Vector, vertex2: Vector, vertex3: Vector, color: Color, material: Material):
        self.vertices = [vertex1, vertex2, vertex3]
        self.color = color
        self.material = material
        
    def __str__(self):
        return f'[ {self.vertices[0]} , {self.vertices[1]} , {self.vertices[2]} ] - Color: {self.color}'

    def normal(self):
        edge1 = self.vertices[1].sub(self.vertices[0])
        edge2 = self.vertices[2].sub(self.vertices[0])
        return edge1.cross(edge2).normalize()

    def intersect(self, ray: Ray):
        # Constante de epsilon para evitar problemas de precisão flutuante
        EPSILON = 1e-6

        # Passo 1: Calcular vetores de borda do triângulo
        edge1 = self.vertices[1].sub(self.vertices[0])
        edge2 = self.vertices[2].sub(self.vertices[0])

        # Passo 2: Calcular vetor H (produto vetorial entre direção do raio e edge2)
        h = ray.direction.cross(edge2)

        # Passo 3: Calcular o fator 'a' (produto escalar entre edge1 e h)
        a = edge1.dot(h)

        # Se 'a' é muito próximo de 0, o raio é paralelo ao triângulo
        if -EPSILON < a < EPSILON:
            return None

        # Passo 4: Calcular a posição relativa U
        f = 1.0 / a
        s = ray.point.sub(self.vertices[0])
        u = f * (s.dot(h))

        # Se U está fora do intervalo [0, 1], não há interseção
        if u < 0.0 or u > 1.0:
            return None

        # Passo 5: Calcular a posição relativa V
        q = s.cross(edge1)
        v = f * ray.direction.dot(q)

        # Se V está fora do intervalo [0, 1], ou U + V > 1, não há interseção
        if v < 0.0 or u + v > 1.0:
            return None

        # Passo 6: Calcular T, a distância do raio até a interseção
        t = f * edge2.dot(q)

        # Se T é negativo, a interseção está atrás do raio, então não é válida
        if t < EPSILON:
            return None

        # Passo 7: Calcular ponto de interseção e normal do triângulo
        intersection_point = ray.point.add(ray.direction.multByScalar(t))
        normal = edge1.cross(edge2).normalize()

        # Retornando informações sobre a interseção
        return {
            "color": self.color,
            "distance": t,
            "normal": normal
        }
