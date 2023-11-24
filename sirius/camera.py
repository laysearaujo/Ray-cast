from ray import Ray

class Camera():
    def __init__(self, location, focous, v_up, distance, width, height):
        self.location = location
        self.v_front = focous.sub(location).normalize()
        self.v_up = v_up
        self.v_right = self.v_front.cross(self.v_up).normalize()
        self.v_up = self.v_right.cross(self.v_front).normalize()
        self.distance = distance
        self.width = width
        self.height = height

    def take(self, scene):
        matrix = []
        for y in range(self.height):
            list_aux = []
            for x in range(self.width):
                ray = self.createRay(x, y)
                color = scene.intersect(ray)
                list_aux.append(color)
            matrix.append(list_aux)
        return matrix       
    
    def createRay(self, x, y):
        vector_final = self.location
        vector_final = vector_final.add(self.v_front.multByScalar(self.distance))  
        vector_final = vector_final.add(self.v_up.multByScalar(self.height/2 - y))
        vector_final = vector_final.add(self.v_right.multByScalar(self.width/2 - x))
        vector_final = vector_final.sub(self.location).normalize()
        return Ray(self.location, vector_final)
