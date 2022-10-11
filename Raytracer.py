from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 512
height = 512

# Materiales

marble = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = OPAQUE)
mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)
rtx = Raytracer(width, height)

rtx.envMap = Texture("parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
#rtx.lights.append( DirectionalLight(direction = (0,0,-1), intensity = 0.5 ))
rtx.lights.append( PointLight(point = (-1,-1,0) ))


rtx.scene.append( Disk(position = (0,-2,-7), radius = 2, normal = (0,1,0), material = mirror ))
rtx.scene.append( Disk(position = (-2.2,1,-7), radius = 1, normal = (0,0,1), material = glass ))
rtx.scene.append( Disk(position = (1.8,1,-7), radius = 1.5, normal = (0,0,1), material = marble ))

rtx.glRender()

rtx.glFinish("output.bmp")