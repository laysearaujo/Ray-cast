class Scene():
    def __init__(self):
        self.spheres = []
        self.planes = []

    def addSphere(self, sphere):
        self.spheres.append(sphere)

    def addPlanes(self, plane):
        self.planes.append(plane)

    def intersect(self, ray):
        distance = float('inf')
        color = None

        for sphere in self.spheres:
            intersect_sphere = sphere.intersect(ray).distance
            if intersect_sphere < distance:
                distance = intersect_sphere
                color = sphere.intersect(ray).color

        for plane in self.planes:
            intersect_plane = plane.intersect(ray).distance
            if intersect_plane < distance:
                distance = intersect_plane
                color = plane.intersect(ray).color

        return (distance, color)
