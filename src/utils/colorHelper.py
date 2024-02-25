from src.graphic.color import Color

def multColor(color1: Color, color2: Color):
    color = Color(0, 0, 0)
    color.r = ((color1.r / 255) * (color2.r / 255)) * 255
    color.g = ((color1.g / 255) * (color2.g / 255)) * 255
    color.b = ((color1.b / 255) * (color2.b / 255)) * 255

    return color

def addColor(color1: Color, color2: Color):
    color = Color(0, 0, 0)
    color.r = ((color1.r / 255) + (color2.r / 255)) * 255
    color.g = ((color1.g / 255) + (color2.g / 255)) * 255
    color.b = ((color1.b / 255) + (color2.b / 255)) * 255

    color.r = min(255, max(0, color.r))
    color.g = min(255, max(0, color.g))
    color.b = min(255, max(0, color.b))

    return color

def multColorByEscalar(color1: Color, escalar: float):
    color = Color(0, 0, 0)
    color.r = ((color1.r / 255) * escalar) * 255
    color.g = ((color1.g / 255) * escalar) * 255
    color.b = ((color1.b / 255) * escalar) * 255

    return color

