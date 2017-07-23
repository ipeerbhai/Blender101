## import the bpy module so I can call blender functions ( bpy == blender python.  It's 3.5.2 )
import bpy

## SISFuncs -- Single Instance Functions -- these are sort of my global ease of use functions.
class SISFuncs:
    def clearAllObjects(self):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        
        
        
class OpenSCADFunctions:
    def cube(self, size=(1,1,1), center=True, name=""):
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
        bpy.context.object.scale = size
        if len(name) > 0:
            bpy.context.object.name = name;

## main execution area.
CommonLib = SISFuncs()
CommonLib.clearAllObjects()

openSCAD = OpenSCADFunctions()
openSCAD.cube(size=(2, 3, 4), name="fucker");

