from Raytracer.Geo import Point
from Raytracer.Geo import Vector
from Raytracer.Ray import Ray
from Raytracer.Plane import Plane
from Raytracer.Triangle import Triangle
from Raytracer.Sphere import Sphere
import numpy
from PIL import Image

kugel = Sphere(Point(200, 200, 400), 100000)
dreieck = Triangle(Point(100, 100, 10), Point(200, 200, 10), Point(300, 100, 10))
ebene = Plane(Point(17, 23, 20), Vector(2, 9, 3))
imageWidth = 400
imageHeight = 400
wRes = 5
hRes = 5
BACKGROUND_COLOR = (0, 0, 0) #konstante für hintergrundfarbe
objectlist = [kugel]#liste der objekte auf die gestrahlt wird
e = Point(0, 1.8, 400) #augenposition
c = Point(0, 3, 0) #augenblickrichtung
up = Vector(0, 1, 0) #upvektor
l = (30, 30, 10) #Lichtquelle, Typ rausfinden
ce = c - e # wird zur berechnung von f benötigt
f = ce / ce.length()
fxup = f.cross(up)
s = fxup / fxup.length()
u = s.cross(f)
img = Image.new('RGB', (imageWidth, imageHeight), BACKGROUND_COLOR)


def calcRay(x,y):  #berechnet einen Strahl aus Bildschirmkoordinaten

    return Ray(e, Point(x, y, 0) - e)



pixelWidth = imageWidth / (wRes -1)
pixelHeight = imageHeight / (hRes - 1)
for y in range(hRes):
    for x in range(wRes):
        xcomp = s * (x*pixelWidth - imageWidth/2)
        ycomp = u * (x*pixelHeight - imageHeight / 2)
        ray = Ray(e, f + xcomp + ycomp)


for x in range(int(pixelWidth)):
    for y in range(int(pixelHeight)):
        ray = calcRay(x,y) #noch zu implementieren
        maxdist = float('inf')
        color = BACKGROUND_COLOR #noch erstellen
        for object in objectlist:
            hitdist = object.intersectionParameter(ray)
            if hitdist:
                if hitdist < maxdist:
                    maxdist = hitdist
                    color = (255, 255, 255)
    img.putpixel((x, y), color)


img.show()
