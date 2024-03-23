from typing import List
from src.geometry.vector import Vector
from src.geometry.ray import Ray
from src.graphic.color import Color

class OctreeNode:
    def __init__(self, bounds):
        self.bounds = bounds
        self.objects = []
        self.children = [None] * 8

    def is_leaf(self):
        return all(child is None for child in self.children)

class Octree:
    def __init__(self, max_objects_per_node=8, max_depth=8):
        self.root = None
        self.max_objects_per_node = max_objects_per_node
        self.max_depth = max_depth

    def build(self, objects):
        # Construir o octree a partir da lista de objetos
        self.root = self._build_recursive(objects, Vector(float('inf'), float('inf'), float('inf')), Vector(float('-inf'), float('-inf'), float('-inf')), self.max_depth)

    def _build_recursive(self, objects, min_bound, max_bound, depth):
        if depth == 0 or len(objects) <= self.max_objects_per_node:
            node = OctreeNode((min_bound, max_bound))
            node.objects = objects
            return node

        mid_point = (min_bound + max_bound) / 2
        children_bounds = [
            (min_bound, mid_point),  # 0: (-x, -y, -z)
            (Vector(mid_point.x, min_bound.y, min_bound.z), Vector(max_bound.x, mid_point.y, mid_point.z)),  # 1: (+x, -y, -z)
            (Vector(min_bound.x, mid_point.y, min_bound.z), Vector(mid_point.x, max_bound.y, mid_point.z)),  # 2: (-x, +y, -z)
            (Vector(mid_point.x, mid_point.y, min_bound.z), Vector(max_bound.x, max_bound.y, mid_point.z)),  # 3: (+x, +y, -z)
            (Vector(min_bound.x, min_bound.y, mid_point.z), Vector(mid_point.x, mid_point.y, max_bound.z)),  # 4: (-x, -y, +z)
            (Vector(mid_point.x, min_bound.y, mid_point.z), Vector(max_bound.x, mid_point.y, max_bound.z)),  # 5: (+x, -y, +z)
            (Vector(min_bound.x, mid_point.y, mid_point.z), Vector(mid_point.x, max_bound.y, max_bound.z)),  # 6: (-x, +y, +z)
            (mid_point, max_bound)  # 7: (+x, +y, +z)
        ]

        children = [self._build_recursive([], child_bounds[0][0], child_bounds[0][1], depth - 1) for child_bounds in children_bounds]

        node = OctreeNode((min_bound, max_bound))
        node.children = children

        for obj in objects:
            for i, child in enumerate(node.children):
                if obj_intersects_bounds(obj, child.bounds):
                    child.objects.append(obj)

        return node

    def insert(self, obj):
        # Inserir um objeto no octree
        self._insert_recursive(obj, self.root, self.max_depth)

    def _insert_recursive(self, obj, node, depth):
        if node.is_leaf():
            node.objects.append(obj)
            if len(node.objects) > self.max_objects_per_node and depth > 0:
                self._subdivide(node)
                for o in node.objects:
                    self._insert_recursive(o, node, depth - 1)
                node.objects = []
        else:
            for child in node.children:
                if obj_intersects_bounds(obj, child.bounds):
                    self._insert_recursive(obj, child, depth - 1)

    def _subdivide(self, node):
        min_bound, max_bound = node.bounds
        mid_point = (min_bound + max_bound) / 2
        children_bounds = [
            (min_bound, mid_point),  # 0: (-x, -y, -z)
            (Vector(mid_point.x, min_bound.y, min_bound.z), Vector(max_bound.x, mid_point.y, mid_point.z)),  # 1: (+x, -y, -z)
            (Vector(min_bound.x, mid_point.y, min_bound.z), Vector(mid_point.x, max_bound.y, mid_point.z)),  # 2: (-x, +y, -z)
            (Vector(mid_point.x, mid_point.y, min_bound.z), Vector(max_bound.x, max_bound.y, mid_point.z)),  # 3: (+x, +y, -z)
            (Vector(min_bound.x, min_bound.y, mid_point.z), Vector(mid_point.x, mid_point.y, max_bound.z)),  # 4: (-x, -y, +z)
            (Vector(mid_point.x, min_bound.y, mid_point.z), Vector(max_bound.x, mid_point.y, max_bound.z)),  # 5: (+x, -y, +z)
            (Vector(min_bound.x, mid_point.y, mid_point.z), Vector(mid_point.x, max_bound.y, max_bound.z)),  # 6: (-x, +y, +z)
            (mid_point, max_bound)  # 7: (+x, +y, +z)
        ]
        node.children = [OctreeNode(child_bounds) for child_bounds in children_bounds]

    def intersect(self, ray):
        # Interseção de raio com o octree
        return self._intersect_recursive(ray, self.root)

    def _intersect_recursive(self, ray, node):
        if node is None:
            return {
            "distance": float('inf'),
            "color": Color(0, 0, 0),
            "normal": None,
            "object_hit": None
        }

        if node.is_leaf():
            closest_intersection = {
                "distance": float('inf'),
                "color": Color(0, 0, 0),
                "normal": None,
                "object_hit": None
            }
            for obj in node.objects:
                intersection = obj.intersect(ray)
                if intersection and intersection["distance"] < closest_intersection["distance"]:
                    closest_intersection = {
                        "distance": intersection["distance"],
                        "color": intersection["color"],
                        "normal": intersection["normal"],
                        "object_hit": obj
                    }
            return closest_intersection
        else:
            closest_intersection = {
                "distance": float('inf'),
                "color": Color(0, 0, 0),
                "normal": None,
                "object_hit": None
            }
            for child in node.children:
                if obj_intersects_bounds(obj, child.bounds):
                    intersection = self._intersect_recursive(ray, child)
                    if intersection and intersection["distance"] < closest_intersection["distance"]:
                        closest_intersection = intersection
            return closest_intersection


def obj_intersects_bounds(obj, bounds):
    min_bound, max_bound = bounds
    # Verificar se o objeto intersecciona com os limites do nó do octree
    obj_min = obj.min_point()  # Função a ser implementada em cada classe de objeto (por exemplo, Sphere, Plane, TriangularMesh)
    obj_max = obj.max_point()  # Função a ser implementada em cada classe de objeto (por exemplo, Sphere, Plane, TriangularMesh)

    # Verificar interseção em cada dimensão (x, y, z)
    intersects_x = obj_max.x >= min_bound.x and obj_min.x <= max_bound.x
    intersects_y = obj_max.y >= min_bound.y and obj_min.y <= max_bound.y
    intersects_z = obj_max.z >= min_bound.z and obj_min.z <= max_bound.z

    # Se houver interseção em todas as dimensões, o objeto intersecta os limites do nó
    return intersects_x and intersects_y and intersects_z

