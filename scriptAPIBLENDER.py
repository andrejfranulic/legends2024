import bpy

class NombreClase(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.nombre_clase"
    bl_label = "# Op1"

    def execute(self, context):
        # Aquí va la lógica de tu operador
        context.object.location.x += 1.0
        return {'FINISHED'}
    
class MiOperador(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.mi_operador"
    bl_label = "# Op2"

    def execute(self, context):
        # Aquí va la lógica de tu operador
        context.object.location.x += 1.0
        return {'FINISHED'}
            
class MiPanel(bpy.types.Panel):
    """Crea un Panel en la región de la barra de herramientas"""
    bl_label = "Panel API"
    bl_idname = "OBJECT_PT_mipanel2"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tools"

    def draw(self, context):
        layout = self.layout
        layout.operator(NombreClase.bl_idname, icon='WORLD_DATA')
        layout.operator(MiOperador.bl_idname, icon='GHOST_ENABLED')

def register():
    bpy.utils.register_class(MiPanel)
    bpy.utils.register_class(NombreClase)
    bpy.utils.register_class(MiOperador)

def unregister():
    bpy.utils.unregister_class(MiPanel)
    bpy.utils.unregister_class(NombreClase)
    
if __name__ == "__main__":
    register()



        