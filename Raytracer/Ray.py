class Ray(object):
    def __init__(self, origin, direction):
        self.origin = origin #Punkt
        self.direction = direction.normalized() #Vektor


    def __repr__(self):
        return "Ray(%s, %s)" %(repr(self.origin), repr(self.direction))

    def pointAtParameter(self, t):
        return self.origin + self.direction * t

