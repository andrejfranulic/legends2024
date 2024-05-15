import bpy
import random as r
class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.op1"
    bl_label = "Crear"

    def execute(self, context):
        # Aquí va la lógica de tu operador
        for i in range(10):
            bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(r.random(),r.random(),r.random()), scale=(.1,.1,.1))
        return {'FINISHED'}

class SimpleOperator2(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.s_op2"
    bl_label = "Borrar"

    def execute(self, context):
        # Aquí va la lógica de tu operador
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
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
    
if __name__ == "__main__":
    register()



        