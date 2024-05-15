import bpy
import random as r

class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.s_p"
    bl_label = "Crear"

    def execute(self, context):
        t = r.randint(10, 15)
        
        bpy.ops.mesh.primitive_plane_add(size=35.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(1, 1, 1))
    
        for i in range(t):
            x = r.uniform(-15, 15)
            y = r.uniform(-15, 15)
            z = r.uniform(-4, 4)
            bpy.ops.mesh.primitive_cube_add(size=2.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(x, y, z), rotation=(0.0, 0.0, 0.0), scale=(1, 1, 5))
        
        return {'FINISHED'}

class SimpleOperator2(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.s_p2"
    bl_label = "Borrar"

    def execute(self, context):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
        return {'FINISHED'}

class SimplePanel(bpy.types.Panel):
    """Crea un Panel en la región de la barra de herramientas"""
    bl_label = "Mi etiqueta"
    bl_idname = "OBJECT_PT_simple"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Mi Panel"

    def draw(self, context):
        layout = self.layout
        layout.operator(SimpleOperator.bl_idname, icon='GHOST_ENABLED')
        layout.operator(SimpleOperator2.bl_idname, icon='GHOST_DISABLED')

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
