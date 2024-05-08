import bpy

def  delete_all_objects():
     bpy.ops.object.select_all(action='SELECT')
     bpy.ops.object.delete()

class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.eliminator"
    bl_label = "Eliminatodo"

    def execute(self, context):
        # Aquí va la lógica de tu operador
        delete_all_objects()
        return {'FINISHED'}
    
class SimplePanel(bpy.types.Panel):
    """Crea un Panel en la región de la barra de herramientas"""
    bl_label = "Panel de exterminazión"
    bl_idname = "OBJECT_PT_simple"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tools"

    def draw(self, context):
        layout = self.layout
        layout.operator(SimpleOperator.bl_idname, icon='REMOVE')

def register():
    bpy.utils.register_class(SimplePanel)
    bpy.utils.register_class(SimpleOperator)

def unregister():
    bpy.utils.unregister_class(SimplePanel)
    bpy.utils.unregister_class(SimpleOperator)
    
if __name__ == "__main__":
    register()



        