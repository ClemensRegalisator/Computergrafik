import math


class Sphere(object):
    def __init__(self, center, radius, color):
        self.center = center     #point
        self.radius = radius     #scalar
        self.color = color

    def __repr(self):
        return "".join("Sphere(" + str(self.center) + ", " + str(self.radius) + ")")

    def intersectionParameter(self, ray):
        co = self.center - ray.origin
        v = co.dot(ray.direction)
        discriminant = v * v - co.dot(co) + self.radius * self.radius
        if discriminant < 0:
            return None
        else:
            return v - math.sqrt(discriminant)

    def normalAt(self, p):
        return (p - self.center).normalized()

    def colorAt(self, ray):
        return self.color
