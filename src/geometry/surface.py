from src.geometry.vector import Vector
from src.graphic.color import Color

import math

class Surface:
    def __init__(self, point: Vector, normal: Vector, color: Color, distance: int):
        self.point = point
        self.normal = normal
        self.color = color
        self.distance = distance
    
    def getReflection(self, direction: Vector):
        tNormal = self.normal.normalize()
        tDirection = direction.normalize()

        return tNormal.multByScalar(2.0 * tNormal.dot(tDirection)).sub(tDirection).normalize()
    

    # Vetor SurfaceIntersection::getRefraction(Vetor direction, double refractionIndex) const {
    # Vetor tNormal = normal.normalize();
    # Vetor tDirection = direction.normalize();

    # if(cmp(tNormal.angle(tDirection), PI/2.0) == 1) tNormal = tNormal * -1.0;

    # double theta1 = tDirection.angle(tNormal);
    # double cosTheta1 = cos(theta1);

    # double ref = 1.0/refractionIndex;

    # double sinTheta1_2 = 1.0 - cosTheta1 * cosTheta1;

    # double cosTheta2 = sqrt(1.0 - ref*ref * sinTheta1_2);

    # Vetor refraction = ((tDirection * -1.0) * ref) + (tNormal * (ref * cosTheta1 - cosTheta2));

    # return refraction.normalize();

    def getRefraction(self, direction: Vector, refractionIndex: float):
        tNormal = self.normal.normalize()
        tDirection = direction.normalize()

        PI = math.acos(-1)
        if tNormal.angle(tDirection) > PI/2:
            tNormal = tNormal.multByScalar(-1)
        
        theta1 = tDirection.angle(tNormal)
        cosTheta1 = math.cos(theta1)

        ref = 1.0/refractionIndex

        sinTheta1_2 = 1.0 - cosTheta1 * cosTheta1

        cosTheta2 = math.sqrt(1.0 - ref * ref * sinTheta1_2)

        refraction = tDirection.multByScalar(-1 * ref).add(tNormal.multByScalar(ref * cosTheta1 - cosTheta2))

        return refraction.normalize()