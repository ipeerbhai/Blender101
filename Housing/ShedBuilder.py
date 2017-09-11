import bpy

## helper function -- converts feet and inches to fractional feet.

def FractionalFeet(feet, inches):
    output = feet + (inches/12)
    return output

## This class is inspired by OpenSCAD, but not really openSCAD.
## I think making a full openSCAD --> blender port would be a lot of work, and someone likely
## did it already.  I'd rather make something lightweight and easy to port/understand.
class OpenSCADFunctions:

    ## in openSCAD, I use cube with size and center attributes often.  
    def cube(self, size=(1,1,1), center=True, name=""):
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
        cube_ref = bpy.context.active_object
        cube_ref.select = True
        cube_ref.draw_type='SOLID'
        cube_ref.dimensions = size
        if len(name) > 0:
            bpy.context.object.name = name;
        return(cube_ref)
    
## Housing is a class that abstracts things like houses, sheds, etc...

class Housing:
    ## I expect the human to help.  So, I'll make the 4 walls, floor, and overlapping roof
    def Shed(self, length=8, width=8, WallHeight = 8):
        WallThicnkess = FractionalFeet(0, 6)
        openSCAD = OpenSCADFunctions()

        ## wall 1
        openSCAD.cube(size=(width - (2*WallThicnkess), WallThicnkess ,WallHeight))
        return None
    
    
    
    
## test cases
def TestFractionalFeet():
    ## create a cube with dimensions 16ft by a6 ft by 8 inches
    openSCAD = OpenSCADFunctions()
    openSCAD.cube(size = (16, 16, FractionalFeet(feet=0, inches=8)))
    return None

#TestFractionalFeet()
House = Housing()
House.Shed()
