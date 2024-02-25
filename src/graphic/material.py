from src.graphic.color import Color

class Material:
    def __init__(self, kd: Color, ks: Color, ka: Color, kr: Color, kt: Color, eta: float):
        self.kd = kd  # Coeficiente difuso
        self.ks = ks  # Coeficiente especular
        self.ka = ka  # Coeficiente ambiental
        self.kr = kr  # Coeficiente de reflexão
        self.kt = kt  # Coeficiente de transmissão
        self.eta = eta  # Coeficiente de rugosidade