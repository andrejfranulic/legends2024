import bpy
import random as r
#esto borra todo
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

for i in range(100):
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(r.random(),r.random(),r.random()), scale=(.1,.1,.1))
