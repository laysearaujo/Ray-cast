from src.graphic.color import Color
from src.entity.sphere import Sphere
from src.entity.plane import Plane
from src.geometry.ray import Ray
from src.geometry.vector import Vector
from src.geometry.triangularMesh import TriangularMesh
from src.geometry.surface import Surface
from src.utils.colorHelper import multColor, addColor, multColorByEscalar
from src.graphic.light import Light
from src.graphic.material import Material

import math

class Scene():
    def __init__(self):
        self.spheres = []
        self.planes = []
        self.meshes = []
        self.lights = []
        self.enviroment = Color(255, 255, 255)

    def addSphere(self, sphere: Sphere):
        self.spheres.append(sphere)

    def addPlane(self, plane: Plane):
        self.planes.append(plane)

    def addMesh(self, mesh: TriangularMesh):
        self.meshes.append(mesh)

    def addLight(self, light: Light):
        self.lights.append(light)

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

    def traceRay(self, ray: Ray, layer: int):
        matched = self.intersect(ray)
        if matched["object_hit"] == None: 
            return Color(0, 0, 0)
        
        point = Vector(ray.direction.x * matched['distance'] + ray.point.x, 
                       ray.direction.y * matched['distance'] + ray.point.y, 
                       ray.direction.z * matched['distance'] + ray.point.z)
        
        surface = Surface(point, matched['normal'], matched['color'], matched['distance'])
        return multColor(matched["color"], self.phong(ray, surface, layer, matched["object_hit"].material))
        

#     color = color + (
#         traceRay(Ray(ray.pointAt(surface.distance + 0.01), surface.getRefraction(ray.direction * -1.0, box.getRefractionIndex())), layer+1)
#             * box.getTransmissionCoefficient()
#     );

#     return color;
# }
    def phong(self, ray: Ray, surface: Surface, layer: int, material: Material):
        if layer > 4: 
            return Color(0, 0, 0)
        
        color = multColor(self.enviroment, material.ka)

        # pegando a contribuicao de todas as luzes no ponto interceptado
        for light in self.lights:
            color = addColor(color, self.brightness(ray, surface, material, light))

        # recursao: refletindo os raios que saem do obsevador
        color = addColor(
            color,
            multColor(
                self.traceRay(
                    Ray(
                        ray.pointAt(
                            surface.distance - 0.01
                        ),
                        surface.getReflection(
                            ray.direction.multByScalar(-1)
                        )
                    ),
                    layer+1
                ),
                material.kr
            )
        )

        color = addColor(
            color,
            multColor(
                self.traceRay(
                    Ray(
                        ray.pointAt(
                            surface.distance + 0.01
                        ),
                        surface.getRefraction(
                            ray.direction.multByScalar(-1.0), 
                            material.ior
                        )
                    ), 
                    layer+1
                ),
                material.kt
            )
        )

        return color
            
    def brightness(self, ray: Ray, surface: Surface, material: Material, light: Light):
        PI = math.acos(-1)
        # checar orientacao da superficie
        if ray.direction.angle(surface.normal.multByScalar(-1)) > PI/2:
            surface.normal = surface.normal.multByScalar(-1)


        # raio da luz para o ponto da superficie interceptada
        matched = ray.pointAt(surface.distance)
        direction = light.position.sub(matched).normalize()

        temp = Ray(matched, direction)

        delta = 0.01

        lightRay = Ray(temp.pointAt(delta), direction)

        opaqueSurface = self.intersect(lightRay)

        toLight = light.position.sub(lightRay.direction)

        # se tem algo  escondendo a luz
        if (opaqueSurface['distance'] + delta) < toLight.norm():
            return Color(0, 0, 0)
        
        color = light.intensity
        
        # se tiver olhando por baixo
        if lightRay.direction.angle(surface.normal) >= PI/2:
            return Color(0, 0, 0)
        
        lightReflex = surface.getReflection(lightRay.direction)

        aux = lightRay.direction.dot(surface.normal)
        diffuse = multColorByEscalar(material.kd, aux)

        aux = pow(lightReflex.dot(ray.direction.multByScalar(-1)), material.eta);
        specular = multColorByEscalar(material.ks, aux)

        color = multColor(color, addColor(diffuse, specular)) 

        return color
    
