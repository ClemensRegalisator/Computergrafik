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
        if type(other) == Vector:
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vector(other * self.x, other * self.y, other * self.z)

    def __rmul__(self, other):
        if type(other) == Vector:
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vector(other * self.x, other * self.y, other * self.z)

    def dot(self, other):
        skalar = self.x * other.x + self.y * other.y + self.z * other.z
        return(skalar)

    def cross(self, other):
        one = [self.x, self.y, self.z]
        two = [other.x, other.y, other.z]
        new = numpy.cross(one, two)
        return Vector(new[0], new[1], new[2])

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalized(self):
        return self / self.length()

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other, self.z / other)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        if type(other) == Point:
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            print("Kein Punkt!")
            raise Exception

    def __add__(self, other):
        if type(other) == Vector:
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return "Error"

    def __radd__(self, other):
        if type(other) == Vector:
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return "Error"

    def __repr__(self):
        return "".join("P(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")")



