from src.graphic.color import Color
from src.entity.sphere import Sphere
from src.entity.plane import Plane
from src.geometry.ray import Ray
from src.geometry.triangularMesh import TriangularMesh

class Scene():
    def __init__(self):
        self.spheres = []
        self.planes = []
        self.meshes = []

    def addSphere(self, sphere: Sphere):
        self.spheres.append(sphere)

    def addPlane(self, plane: Plane):
        self.planes.append(plane)

    def addMesh(self, mesh: TriangularMesh):
        self.meshes.append(mesh)

    def intersect(self, ray: Ray):
        closest_intersection = {
            "distance": float('inf'),
            "color": Color(0, 0, 0),
            "normal": None,
            "object_hit": None
        }

        # Verificar interseções com esferas
        for sphere in self.spheres:
            intersection = sphere.intersect(ray)
            if intersection["distance"] < closest_intersection["distance"]:
                closest_intersection = {
                    "distance": intersection["distance"],
                    "color": intersection["color"],
                    "normal": intersection["normal"],
                    "object_hit": sphere
                }

        # Verificar interseções com planos
        for plane in self.planes:
            intersection = plane.intersect(ray)
            if intersection["distance"] < closest_intersection["distance"]:
                closest_intersection = {
                    "distance": intersection["distance"],
                    "color": intersection["color"],
                    "normal": intersection["normal"],
                    "object_hit": plane
                }

        # Verificar interseções com malhas triangulares
        for mesh in self.meshes:
            intersection = mesh.intersect(ray)
            if intersection and intersection["distance"] < closest_intersection["distance"]:
                closest_intersection = {
                    "distance": intersection["distance"],
                    "color": intersection["color"],
                    "normal": intersection["normal"],
                    "object_hit": mesh
                }

        return closest_intersection
