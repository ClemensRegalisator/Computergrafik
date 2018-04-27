from Raytracer.Geo import Point
from Raytracer.Geo import Vector
from Raytracer.Ray import Ray
from Raytracer.Plane import *
from Raytracer.Triangle import Triangle
from Raytracer.Sphere import Sphere
from PIL import Image
import math
import time

#initialisierung
    #bild
REFLECTION = 0.3
MAX_LEVEL = 10
imageHeight = 1080
imageWidth = 1920
wRes = 5
hRes = 5
BACKGROUND_COLOR = Vector(0, 0, 0) #konstante für hintergrundfarbe
SCHATTIG = (0, 0, 0)
fieldOfView = math.pi / 8   #öffnungswinkel
aspectRatio = imageWidth / imageHeight
height = 2 * math.tan(fieldOfView / 2)
width = aspectRatio * height

pixelWidth = width / (imageWidth - 1)
pixelHeight = height / (imageHeight - 1)

img = Image.new('RGB', (imageWidth, imageHeight), (BACKGROUND_COLOR.x, BACKGROUND_COLOR.y, BACKGROUND_COLOR.z))

    #objekte
s1 = Sphere(Point(40, 0, 1), 2, (0, 255, 0))
s2 = Sphere(Point(40, 3, -2), 2, (255, 0, 0))
s3 = Sphere(Point(40, -3, -2), 2, (0, 0, 255))
t1 = Triangle(Point(40, 3, -2), Point(40, -3, -2), Point(40, 0, 1), (255, 255, 0))
e1 = Plane(Point(0, 0, -7), Vector(0, 0, 1), (0, 255, 0), True)
objectlist = [e1, s1, s2, s3, t1]            #liste der objekte auf die gestrahlt wird

    #kamera
e = Point(0, 0, 0)   #augenposition
c = Point(20, 0, 0)      #augenblickrichtung
up = Vector(0, 0, 1)    #upvektor
lightsource = Point(0, 0, 20)        #Lichtquelle
ce = c - e              #wird zur berechnung von f benötigt
f = ce / ce.length()
fxup = f.cross(up)
s = fxup / fxup.length()
u = s.cross(f)


#lichtfarben
ca = Vector(50, 50,50)



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



def phong(schnittpunkt, ray, object):
    ka = 0.3
    kd = 0.6
    ks = 0.3

    lv = (lightsource - schnittpunkt).normalized()
    n = (object.normalAt(schnittpunkt)).normalized()
    lr = (lv.cross(n)).normalized()
    d = ray.direction.normalized()
    if type(object) == Plane:
        cin = Vector(object.colorAt(schnittpunkt)[0], object.colorAt(schnittpunkt)[1], object.colorAt(schnittpunkt)[2])
    else:
        cin = Vector(object.colorAt(ray)[0], object.colorAt(ray)[1], object.colorAt(ray)[2])
    amb = ca * ka
    dif = cin * (kd * lv.dot(n))
    spek = cin * (ks * (lr.dot(d * (-1)) ** 2))
    rgb = amb + dif + spek
    if schatten(schnittpunkt):
        return Vector(int(rgb.x / 1.7), int(rgb.y / 1.7), int(rgb.z / 1.7))
    return Vector(int(rgb.x), int(rgb.y), int(rgb.z))


def intersect(ray, level):
    if level >= MAX_LEVEL:
        return None
    aktObj = None
    maxdist = float('inf')
    for object in objectlist:
        hitdist = object.intersectionParameter(ray)
        if hitdist:
            if 0 < hitdist < maxdist:
                maxdist = hitdist
                aktObj = object
    if maxdist == float('inf'):
        return None
    else:
        return (ray.origin + ray.direction * maxdist, aktObj)


def computeReflectedRay(hitPointData, ray):
    n = hitPointData[1].normalAt(hitPointData[0])
    newRay = (ray.direction - 2 * n.dot(ray.direction) * n)
    return Ray(hitPointData[0], newRay)

def shade(level, hitPointData, ray):


    directColor = phong(hitPointData[0], ray, hitPointData[1])
    reflectedRay = computeReflectedRay(hitPointData, ray)
    reflectedColor = traceRay(level + 1, reflectedRay)



    return directColor + REFLECTION * reflectedColor


def traceRay(level, ray):
    hitPointData = intersect(ray, level)
    if hitPointData:
        return shade(level, hitPointData, ray)
    return BACKGROUND_COLOR


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
                        color = phong(schnittpunkt, ray, object)
                        if schatten(schnittpunkt):
                            color = (int(color[0] / 1.7), int(color[1] / 1.7), int(color[2] / 1.7))

            img.putpixel((imageWidth - 1 - x, imageHeight - 1 - y), color)
        if x % progress == 0:
            print("Fortschritt: " + str((x / imageWidth) * 100) + "%")

def cheese2():
    progress = imageWidth / 10
    for x in range(imageWidth):
        for y in range(imageHeight):
            ray = calcRay(x, y)              #noch zu implementieren
            color = traceRay(0, ray)
            color = (int(color.x), int(color.y), int(color.z))
            img.putpixel((imageWidth - 1 - x, imageHeight - 1 - y), color)
        if x % progress == 0:
            print("Fortschritt: " + str((x / imageWidth) * 100) + "%")

a = time.time()
cheese2()
print(time.time() - a)
img.show()
