import bpy
import random 
class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.s_p"
    bl_label = "Crear"

    def execute(self, context):
   
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
            
        
        return{'FINISHED'}
    
class SimpleOperator2(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.s_x"
    bl_label = "Delete"

    def execute(self, context):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        return {'FINISHED'}
        
        
        
    
class SimplePanel(bpy.types.Panel):
   
    bl_label = "Piramide de cubos"
   
    bl_idname = "OBJECT_PT_simple"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Object random"

    def draw(self, context):
        layout = self.layout
        layout.operator(SimpleOperator.bl_idname, icon='GHOST_ENABLED')
        layout.operator(SimpleOperator2.bl_idname, icon='REMOVE')
   
       

def register():
    bpy.utils.register_class(SimplePanel)
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(SimpleOperator2)

def unregister():
    bpy.utils.unregister_class(SimplePanel)
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(SimpleOperator2)
    
if __name__ == "__main__":
    register()



        
