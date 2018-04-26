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
s1 = Sphere(Point(40, 0, 1), 2, (0, 255, 0))
s2 = Sphere(Point(40, 3, -2), 2, (255, 0, 0))
s3 = Sphere(Point(40, -3, -2), 2, (0, 0, 255))
t1 = Triangle(Point(40, 3, -2), Point(40, -3, -2), Point(40, 0, 1), (255, 255, 0))
e1 = Plane(Point(0, 0, -7), Vector(0, 0, 1), (0, 128, 128))
objectlist = [e1, s1, s2, s3]            #liste der objekte auf die gestrahlt wird

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
    cin = Vector(object.colorAt(ray)[0], object.colorAt(ray)[1], object.colorAt(ray)[2])
    amb = ca * ka
    dif = cin * (kd * lv.dot(n))
    spek = cin * (ks * (lr.dot(d * (-1)) ** 2))
    rgb = amb + dif + spek
    return (int(rgb.x), int(rgb.y), int(rgb.z))





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
                            color = phong(schnittpunkt, ray, object)
            img.putpixel((imageWidth - 1 - x, imageHeight - 1 - y), color)
        if x % progress == 0:
            print("Fortschritt: " + str((x / imageWidth) * 100) + "%")
'''
def intersect(level, ray, maxlevel):
    return 0


def traceRay(level, ray):
    hitpointData = intersect(level, ray, maxlevel)

def shade(level, hitpointData,ray, object):
    directColor = phong(hitpointData, ray, object)

    reflectedRay = computeReflectedRay(hitpointData)
    reflectColor = traceRay(level+1, reflectedRay)
'''
a = time.time()
cheese()
print(time.time() - a)
img.show()
