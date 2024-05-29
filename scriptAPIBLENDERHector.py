import bpy
import random as r

def  delete_all_objects():
     bpy.ops.object.select_all(action='SELECT')
     bpy.ops.object.delete()
    
def  create_objects():
     RX=r.randint(-30,30)
     RY=r.randint(-30,30)
     RZ=r.randint(-30,30)
     TRX=r.randint(1,5)
     TRY=r.randint(1,5)
     TRZ=r.randint(1,5)
     bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(RX, RY, RZ), scale=(TRX, TRY, TRZ))


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.eliminator"
    bl_label = "Eliminatodo"
    
    def execute(self, context):
        # Aquí va la lógica de tu operador
        delete_all_objects()
        return {'FINISHED'}
    
class SimpleOperator2(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.creator"
    bl_label = "Creador"    
    
    def execute(self, context):
        # Aquí va la lógica de tu operador
        create_objects()
        return {'FINISHED'}
    
class SimplePanel(bpy.types.Panel):
    """Crea un Panel en la región de la barra de herramientas"""
    bl_label = "Panel de exterminazión y creación"
    bl_idname = "OBJECT_PT_simple"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Cre y dest"
    

    def draw(self, context):
        layout = self.layout
        layout.operator(SimpleOperator.bl_idname, icon='REMOVE')
        layout.operator(SimpleOperator2.bl_idname, icon='PLUS')

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



        