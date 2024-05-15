import bpy

class ListObjectsOperator(bpy.types.Operator):
    """Lista los objetos en un informe"""
    bl_idname = "object.list_objects"
    bl_label = "Listar Objetos"
    
    def execute(self, context):
        # Lógica para listar los objetos
        objects_list = "Objetos en la escena:\n"
        for obj in bpy.context.scene.objects:
            objects_list += f"{obj.name}\n"
        self.report({'INFO'}, "Lista de objetos mostrada en el panel")
        context.scene.objects_list = objects_list
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
        layout.operator(ListObjectsOperator.bl_idname, icon='OBJECT_DATAMODE')
        if hasattr(context.scene, "objects_list"):
            layout.label(text="Lista de objetos:")
            for line in context.scene.objects_list.split('\n'):
                layout.label(text=line)

def register():
    bpy.utils.register_class(ListObjectsOperator)
    bpy.utils.register_class(SimplePanel)
    bpy.types.Scene.objects_list = bpy.props.StringProperty(name="Objects List", default="")

def unregister():
    bpy.utils.unregister_class(ListObjectsOperator)
    bpy.utils.unregister_class(SimplePanel)
    del bpy.types.Scene.objects_list
    
if __name__ == "__main__":
    register()
