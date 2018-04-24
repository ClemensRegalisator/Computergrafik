from Raytracer.Geo import Point
from Raytracer.Geo import Vector
from Raytracer.Ray import Ray
from Raytracer.Plane import Plane
from Raytracer.Triangle import Triangle
from Raytracer.Sphere import Sphere
from PIL import Image
import math

#initialisierung
    #bild
imageHeight = 1080
imageWidth = 1920
wRes = 5
hRes = 5
BACKGROUND_COLOR = (0, 0, 0) #konstante für hintergrundfarbe
fieldOfView = math.pi / 8   #öffnungswinkel
aspectRatio = imageWidth / imageHeight
height = 2 * math.tan(fieldOfView / 2)
width = aspectRatio * height

pixelWidth = width / (imageWidth - 1)
pixelHeight = height / (imageHeight - 1)

img = Image.new('RGB', (imageWidth, imageHeight), BACKGROUND_COLOR)

    #objekte
s1 = Sphere(Point(40, 0, -3), 2, (0, 255, 0))
s2 = Sphere(Point(40, 3, 0), 2, (255, 0, 0))
s3 = Sphere(Point(40, -3, 0), 2, (0, 0, 255))
t1 = Triangle(Point(40, 3, 0), Point(40, -3, 0), Point(40, 0, -3), (128, 128, 0))
e1 = Plane(Point(0, 0, 0), Vector(0, 0, 1), (0, 128, 128))
objectlist = [s1, s2, s3, t1]            #liste der objekte auf die gestrahlt wird

    #kamera
e = Point(0, 0, 0)   #augenposition
c = Point(20, 0, 0)      #augenblickrichtung
up = Vector(0, 0, 1)    #upvektor
l = (30, 30, 10)        #Lichtquelle, Typ rausfinden
ce = c - e              #wird zur berechnung von f benötigt
f = ce / ce.length()
fxup = f.cross(up)
s = fxup / fxup.length()
u = s.cross(f)


def calcRay(x,y):      #berechnet einen Strahl aus Bildschirmkoordinaten
    xcomp = s * (x * pixelWidth - width / 2)
    ycomp = u * (y * pixelHeight - height / 2)
    ray = Ray(e, (f + xcomp) + ycomp)
    return ray


def cheese():
    for x in range(imageWidth):
        for y in range(imageHeight):
            ray = calcRay(x, y)              #noch zu implementieren
            maxdist = float('inf')
            color = BACKGROUND_COLOR            #noch erstellen
            for object in objectlist:
                hitdist = object.intersectionParameter(ray)
                if hitdist:
                    if hitdist < maxdist:
                        maxdist = hitdist
                        color = object.colorAt(ray)
            img.putpixel((x, y), color)



cheese()
img.show()
