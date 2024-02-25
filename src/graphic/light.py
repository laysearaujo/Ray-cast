from src.graphic.color import Color
from src.geometry.vector import Vector

class Light:
    def __init__(self, position: Vector, intensity: Color):
        self.position = position  # Posição da luz (Vector)
        self.intensity = intensity  # Intensidade da luz (cor RGB)