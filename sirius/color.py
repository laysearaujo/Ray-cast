class Color:
    def __init__(self, r: float, g: float, b: float):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f'#{self.r:02x}{self.g:02x}{self.b:02x}'