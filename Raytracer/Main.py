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

wRes = 5
hRes = 5
BACKGROUND_COLOR = (0, 0, 0) #konstante für hintergrundfarbe

fieldOfView = math.pi / 8     #öffnungswinkel
aspectRatio = 16/9
imageHeight = int(2 * math.tan(fieldOfView / 2))
imageWidth = int(aspectRatio * imageHeight)
pixelWidth = imageWidth / (wRes - 1)
pixelHeight = imageHeight / (hRes - 1)


img = Image.new('RGB', (imageWidth, imageHeight), BACKGROUND_COLOR)

    #objekte
kugel = Sphere(Point(0, 180, 100), 100)
dreieck = Triangle(Point(100, 100, 10), Point(200, 200, 10), Point(300, 100, 10))
ebene = Plane(Point(17, 23, 20), Vector(2, 9, 3))
objectlist = [kugel]    #liste der objekte auf die gestrahlt wird

    #kamera
e = Point(0, 1.8, 10)   #augenposition
c = Point(0, 3, 0)      #augenblickrichtung
up = Vector(0, 1, 0)    #upvektor
l = (30, 30, 10)        #Lichtquelle, Typ rausfinden
ce = c - e              #wird zur berechnung von f benötigt

f = ce / ce.length()
fxup = f.cross(up)
s = fxup / fxup.length()
u = s.cross(f)




def calcRay(x,y):  #berechnet einen Strahl aus Bildschirmkoordinaten
    xcomp = s * (x * pixelWidth - width / 2)
    ycomp = u * (x * pixelHeight - height / 2)
    ray = Ray(e, f + xcomp + ycomp)
    return ray

for x in range(imageWidth):
    for y in range(imageHeight):
        ray = calcRay(x,y) #noch zu implementieren
        maxdist = float('inf')
        color = BACKGROUND_COLOR #noch erstellen
        for object in objectlist:
            hitdist = object.intersectionParameter(ray)
            if hitdist:
                if hitdist < maxdist:
                    maxdist = hitdist
                    color = object.colorAt(ray)
    img.putpixel((x, y), color)


img.show()
