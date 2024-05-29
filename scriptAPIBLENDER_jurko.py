import bpy
import random

a = 5

x = 0
nx = -50
px = 50
    
for i in range(a):
    y = 0
    ny = -50
    py = 50
    
    for j in range(a):
        bpy.ops.mesh.primitive_plane_add(size=120, enter_editmode=False, align='WORLD', location=(x, y, 0), scale=(1, 1, 1))

        for i in range(10):
            bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(random.randint(nx,px), random.randint(ny,py), 0), scale=(random.randint(1,10), random.randint(1,10), random.randint(1,30)))
        
        y += 120
        ny += 120
        py += 120
        
    x += 120
    nx += 120
    px += 120
