from Raytracer.Geo import Point
from Raytracer.Geo import Vector
from Raytracer.Ray import Ray
from Raytracer.Plane import Plane
from Raytracer.Triangle import Triangle
from Raytracer.Sphere import Sphere
import numpy
from PIL import Image

imageWidth = 400
imageHeight = 400
wRes = 5
hRes = 5
BACKGROUND_COLOR = (0, 0, 0) #konstante für hintergrundfarbe
objectlist = list()
e = Point(0, 1.8, 10)
c = Point(0, 3, 0)
up = Vector(0, 1, 0)


img = Image.new('RGB', (imageWidth,imageHeight ), BACKGROUND_COLOR)


def calcRay(x,y):  #berechnet einen Strahl aus Bildschirmkoordinaten

    return Ray(e, Point(x, y, 0) - e)

def rayCasting():
    for x in range(imageWidth):
        for y in range(imageHeight):
            ray = calcRay(x,y) #noch zu implementieren
            maxdist = float('inf')  #???
            color = BACKGROUND_COLOR #noch erstellen
            for object in objectlist:
                hitdist = object.intersectionParameter(ray)
                if hitdist:
                    if hitdist < maxdist:
                        maxdist = hitdist
                        color = object.colorAt(ray)
        img.putpixel((x, y), color)


img.show()
