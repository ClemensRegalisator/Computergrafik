from Raytracer.Geo import *
class Plane(object):
    def __init__(self, point, normal, color, checker: bool):
        self.point = point #point
        self.normal = normal.normalized() #vector
        self.color = color
        self.checker = checker
        if checker:
            self.baseColor = (255, 255, 255)
            self.otherColor = (0, 0, 0)
            self.ambientCoefficient = 1.0
            self.diffuseCoefficient = 0.6
            self.specularCoefficient = 0.2
            self.checkSize = 1

    def __repr__(self):
        return 'Plane(%s,%s)' %(repr(self.point), repr(self.normal))

    def intersectionParameter(self, ray):
        op = ray.origin - self.point
        a = op.dot(self.normal)
        b = ray.direction.dot(self.normal)
        if b:
            return -a/b
        else:
            return None

    def normalAt(self, p):
        return self.normal

    def colorAt(self, p):
        if self.checker:
            v = Vector(p.x, p.y, p.z)
            v = v * (1.0 / self.checkSize)
            if (int(abs(v.x) + 0.5) + int(abs(v.y) + 0.5) + int(abs(v.z) + 0.5)) % 2:

                return self.otherColor

            return self.baseColor
        return self.color

