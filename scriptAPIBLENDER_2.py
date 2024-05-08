import bpy

# Panel para mostrar la entrada y salida de texto
class TEXT_IO_PT_Panel(bpy.types.Panel):
    bl_label = "Entrada y Salida de Texto"
    bl_idname = "TEXT_IO_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Mi Addon'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Campo de entrada de texto
        layout.prop(scene, "my_text_input")

        # Botón para procesar el texto (ejemplo simple que solo copia la entrada a la salida)
        layout.operator("textio.process", text="Procesar Texto")

        # Muestra el texto de salida
        layout.label(text="Texto de Salida:")
        layout.label(text=scene.my_text_output, icon='INFO')

# Operador para procesar el texto
class TEXT_IO_OT_Process(bpy.types.Operator):
    bl_idname = "textio.process"
    bl_label = "Procesar Texto"

    def execute(self, context):
        # Copia el texto de entrada a la salida como un ejemplo simple
        context.scene.my_text_output = context.scene.my_text_input
        return {'FINISHED'}

# Registro de clases y propiedades
def register():
    bpy.utils.register_class(TEXT_IO_OT_Process)
    bpy.utils.register_class(TEXT_IO_PT_Panel)
    bpy.types.Scene.my_text_input = bpy.props.StringProperty(name="Texto de Entrada")
    bpy.types.Scene.my_text_output = bpy.props.StringProperty(name="Texto de Salida")

def unregister():
    bpy.utils.unregister_class(TEXT_IO_OT_Process)
    bpy.utils.unregister_class(TEXT_IO_PT_Panel)
    del bpy.types.Scene.my_text_input
    del bpy.types.Scene.my_text_output

if __name__ == "__main__":
    register()
