## import the bpy module so I can call blender functions ( bpy == blender python.  It's 3.5.2 )
import bpy
import pdb

## SISFuncs -- Single Instance Functions -- these are sort of my global ease of use functions.
class SISFuncs:

    def deleteActiveOjbects(self):
        o = None
        if bpy.context.active_object is not None:
            if bpy.context.active_object.mode is not 'OBJECT': 
                bpy.ops.object.mode_set(mode = 'OBJECT')
            o = bpy.context.active_object 
            if o.type == 'MESH':
                mesh = o.data
                bpy.context.scene.objects.unlink(o)
                bpy.data.objects.remove(o)
                bpy.data.meshes.remove(mesh)
            else:
                bpy.context.scene.objects.unlink(o)
                bpy.data.objects.remove(o)
                
    def clearAllObjects(self):
        bpy.ops.object.select_all()
        if bpy.context.active_object is not None:
            if bpy.context.active_object.mode is not 'OBJECT':
                bpy.ops.object.mode_set(mode = 'OBJECT')
        for o in bpy.context.scene.objects:
            if o.type == 'MESH':
                mesh = o.data
                bpy.context.scene.objects.unlink(o)	
                bpy.data.objects.remove(o)
                bpy.data.meshes.remove(mesh)
            else:
                bpy.context.scene.objects.unlink(o)
                bpy.data.objects.remove(o)        

    def listAllObjects(self):
        for obj in bpy.data.objects:
            print(obj.name)
            
    def deleteObject(self, objectToDelete):
        bpy.ops.object.select_all(action = 'DESELECT')
        bpy.context.scene.objects.active = objectToDelete
        self.deleteActiveOjbects()

        
## This class is inspired by OpenSCAD, but not really openSCAD.
## I think making a full openSCAD --> blender port would be a lot of work, and someone likely
## did it already.  I'd rather make something lightweight and easy to port/understand.
class OpenSCADFunctions:

    ## in openSCAD, I use cube with size and center attributes often.  
    def cube(self, size=(1,1,1), center=True, name=""):
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
        bpy.context.object.scale = size
        if len(name) > 0:
            bpy.context.object.name = name;
        cube_ref = bpy.context.active_object
        cube_ref.select = True
        cube_ref.draw_type='SOLID'
        return(cube_ref)

    ## define a sphere like openSCAD's, but a little different.
    ## seems to be a UV sphere in blender
    def sphere(self, r=-1, location=(0,0,0)):
        if r >= 0:
            ## valid radius.
            bpy.ops.mesh.primitive_uv_sphere_add(size=r, location=location)
        else:
            raise ValueError('r is not a valid number')
        sphere_ref = bpy.context.active_object
        return(sphere_ref)

    
    def difference(self, source_object, modifier_object):
        CommonLib = SISFuncs()
        ## difference in blender is a boolean modifier between 2 objects
        ## the steps are:
        ## select the object
        ## add a modifier to it
        ## apply the modifier
        ## delete the secondary object to be more openscad-esque.
        
        ## select the object
        bpy.ops.object.select_all(action = 'DESELECT')
        bpy.context.scene.objects.active = source_object
        
        ## add the boolean modifier to the selected object and apply it.
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
        bpy.context.object.modifiers["Boolean"].object = modifier_object
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
        
        ## delete the other object.
        #CommonLib.deleteObject(modifier_object)
        #modifier_object.hide = True
        

## main execution area.
CommonLib = SISFuncs()
CommonLib.listAllObjects()
CommonLib.clearAllObjects()

openSCAD = OpenSCADFunctions()

openSCAD.difference(openSCAD.cube(size=(2,3,4)), openSCAD.sphere(r=2, location=(2,2,2)))

