from ..entity.triangle import Triangle

class TriangularMesh:
    def __init__(self):
        self.triangles = []  # Lista de triângulos na malha

    def addTriangle(self, triangle: Triangle):
        self.triangles.append(triangle)

    def intersectRay(self, ray):
        closest_hit = float('inf')
        hit_color = None
        hit_normal = None

        for triangle in self.triangles:
            # Encontrar a interseção do raio com o plano do triângulo
            intersection_info = triangle.intersect(ray)

            if intersection_info["hit"]:
                # Verificar se o ponto de interseção está dentro do triângulo
                intersection_point = intersection_info["point"]
                is_inside = triangle.isPointInside(intersection_point)

                if is_inside and intersection_info["distance"] < closest_hit:
                    closest_hit = intersection_info["distance"]
                    hit_color = intersection_info["color"]
                    hit_normal = intersection_info["normal"]

        if hit_color:
            return {
                "color": hit_color,
                "normal": hit_normal,
                "distance": closest_hit
            }
        else:
            return {
                "color": None,
                "normal": None,
                "distance": float('inf')
            }