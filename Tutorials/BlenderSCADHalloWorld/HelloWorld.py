import bpy
import blenderscad

## init blenderscad and its namespace
blenderscad.initns(globals())

## we can now begin using blenderscad.
difference(cube((3,3,3), center=True), cylinder(r=1, h=100, fn=100))
