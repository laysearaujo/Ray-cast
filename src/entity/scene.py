from ..graphic.color import Color

class Scene():
    def __init__(self):
        self.spheres = []
        self.planes = []

    def addSphere(self, sphere):
        self.spheres.append(sphere)

    def addPlane(self, plane):
        self.planes.append(plane)

    def intersect(self, ray):
        closest_intersection = {
            "distance": float('inf'),
            "color": Color(0, 0, 0),
            "object_hit": None
        }

        for sphere in self.spheres:
            intersection = sphere.intersect(ray)
            if intersection["distance"] < closest_intersection["distance"]:
                closest_intersection["distance"] = intersection["distance"]
                closest_intersection["color"] = intersection["color"]
                closest_intersection["object_hit"] = sphere

        for plane in self.planes:
            intersection = plane.intersect(ray)
            if intersection["distance"] < closest_intersection["distance"]:
                closest_intersection["distance"] = intersection["distance"]
                closest_intersection["color"] = intersection["color"]
                closest_intersection["object_hit"] = plane

        return closest_intersection
