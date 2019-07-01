from Geo import *
import random
class Plane(object):
    def __init__(self, point, normal, color, checker: bool, random:bool):
        self.point = point #point
        self.normal = normal.normalized() #vector
        self.color = color
        self.checker = checker
        self.random = random
        if checker:
            self.baseColor = (255, 255, 255)
            self.otherColor = (0, 0, 0)
            self.checkSize = 10

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
        if(self.random):
            return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if self.checker:
            v = Vector(p.x, p.y, p.z)
            v = v * (1.0 / self.checkSize)
            if (int(abs(v.x) + 0.5) + int(abs(v.y) + 0.5) + int(abs(v.z) + 0.5)) % 2:
                return self.otherColor
            return self.baseColor
        return self.color
