import numpy
import math


class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "".join("V(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")")

    def __add__(self, other):
        if type(other) is Vector:
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        if type(other) is Point:
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return "Fail"

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector(other * self.x, other * self.y, other * self.z)

    def dot(self, other):
        skalar = self.x * other.x + self.y * other.y + self.z * other.z
        return(skalar)

    def cross(self, other):
        return numpy.cross(self, other)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalized(self):
        return self / self.length

    def __truediv__(self, other):
        return(self.x / other, self.y / other, self.z / other)


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        if type(other) == Vector:
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return "Error"

    def __repr__(self):
        return "".join("P(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")")
