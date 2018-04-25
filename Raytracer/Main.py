from Raytracer.Geo import Point
from Raytracer.Geo import Vector
from Raytracer.Ray import Ray
from Raytracer.Plane import Plane
from Raytracer.Triangle import Triangle
from Raytracer.Sphere import Sphere
from PIL import Image
import math
import time

#initialisierung
    #bild
imageHeight = 400
imageWidth = 400
wRes = 5
hRes = 5
BACKGROUND_COLOR = (255, 255, 255) #konstante für hintergrundfarbe
SCHATTIG = (0, 0, 0)
fieldOfView = math.pi / 8   #öffnungswinkel
aspectRatio = imageWidth / imageHeight
height = 2 * math.tan(fieldOfView / 2)
width = aspectRatio * height

pixelWidth = width / (imageWidth - 1)
pixelHeight = height / (imageHeight - 1)

img = Image.new('RGB', (imageWidth, imageHeight), BACKGROUND_COLOR)

    #objekte
s1 = Sphere(Point(40, 0, 3), 2, (0, 255, 0))
s2 = Sphere(Point(40, 3, 0), 2, (255, 0, 0))
s3 = Sphere(Point(40, -3, 0), 2, (0, 0, 255))
t1 = Triangle(Point(40, 3, 0), Point(40, -3, 0), Point(40, 0, -3), (128, 128, 0))
e1 = Plane(Point(0, 0, -7), Vector(0, 0, 1), (0, 128, 128))
objectlist = [s1, s2, s3, e1]            #liste der objekte auf die gestrahlt wird

    #kamera
e = Point(0, 0, 0)   #augenposition
c = Point(20, 0, 0)      #augenblickrichtung
up = Vector(0, 0, 1)    #upvektor
lightsource = Point(0, 0, 10)        #Lichtquelle
ce = c - e              #wird zur berechnung von f benötigt
f = ce / ce.length()
fxup = f.cross(up)
s = fxup / fxup.length()
u = s.cross(f)

#lichtfarben
ca = Vector(205, 149, 12)
cin = Vector(200, 100, 30)


def schatten(punkt):
    r = Ray(punkt, lightsource - punkt)
    for object in objectlist:
        a = object.intersectionParameter(r)
        if a and a > 0.0001:
            return True
    return False


def calcRay(x,y):      #berechnet einen Strahl aus Bildschirmkoordinaten
    xcomp = s * (x * pixelWidth - width / 2)
    ycomp = u * (y * pixelHeight - height / 2)
    ray = Ray(e, (f + xcomp) + ycomp)
    return ray

def phong(schnittpunkt, ray):
    ka = 0.4
    kd = 0.4
    ks = 0.4
    lv = (lightsource - schnittpunkt).normalized()
    n = (e - schnittpunkt).normalized()
    lr = (lv.cross(n)).normalized()
    d = ray.direction.normalized()

    cout = (ca * ka) + (cin * kd) + lv.dot(n) + (cin * ks) * (lr.dot(d * (-1)) * n)
    rgb = (cout.x, cout.y. cout.z)
    for ele in rgb:
        if ele < 0:
            ele = 0
        if ele > 255:
            ele = 255


    return rgb



def cheese():
    progress = imageWidth / 10
    for x in range(imageWidth):
        for y in range(imageHeight):
            ray = calcRay(x, y)              #noch zu implementieren
            maxdist = float('inf')
            color = BACKGROUND_COLOR            #noch erstellen
            for object in objectlist:
                hitdist = object.intersectionParameter(ray)
                if hitdist:
                    if 0 < hitdist < maxdist:
                        maxdist = hitdist
                        schnittpunkt = ray.origin + ray.direction * hitdist
                        if schatten(schnittpunkt):
                            color = SCHATTIG
                        else:
                            color = phong(schnittpunkt, ray)
            img.putpixel((imageWidth - 1 - x, imageHeight - 1 - y), color)
        if x % progress == 0:
            print("Fortschritt: " + str((x / imageWidth) * 100) + "%")


a = time.time()
cheese()
print(time.time() - a)
img.show()
