import bpy
import random


"""Boton dar tamaño a ciudad"""


# Panel para mostrar la entrada y salida de texto
class TEXT_IO_PT_Panel(bpy.types.Panel):
    bl_label = "Botonitos"
    bl_idname = "TEXT_IO_PT_Panel"
    bl_idname1 = "object.simple_operator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Herramientas'


    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Botón para procesar el texto (ejemplo simple que solo copia la entrada a la salida)
        layout.operator("textio.process", text="Crear Ciudad")

        # Botón para procesar el texto (ejemplo simple que solo copia la entrada a la salida)
        layout.operator("object.simple_operator", text="Borrar Ciudad")

# Operador para procesar el texto
class TEXT_IO_OT_Process(bpy.types.Operator):
    bl_idname = "textio.process"
    bl_label = "Crear Ciudad"

    def execute(self, context):
        # Aquí va la lógica de tu operador
        """Crear Ciudad"""
        a = 2
        x = 0
        nx = -50
        px = 50
            
        for i in range(a):
            y = 0
            ny = -50
            py = 50
            
            for j in range(a):
                bpy.ops.mesh.primitive_plane_add(size=120, enter_editmode=False, align='WORLD', location=(x, y, 0), scale=(1, 1, 1))

                for i in range(50):
                    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(random.randint(nx,px), random.randint(ny,py), 0), scale=(random.randint(1,10), random.randint(1,10), random.randint(1,30)))
                
                y += 120
                ny += 120
                py += 120
                
            x += 120
            nx += 120
            px += 120
        return {'FINISHED'}

class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Borrar Ciudad"
    
    def execute(self, context):
        # Aquí va la lógica de tu operador
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        return {'FINISHED'}

        
# Registro de clases y propiedades
def register():
    bpy.utils.register_class(TEXT_IO_OT_Process)
    bpy.utils.register_class(TEXT_IO_PT_Panel)
    bpy.utils.register_class(SimpleOperator)


def unregister():
    bpy.utils.unregister_class(TEXT_IO_OT_Process)
    bpy.utils.unregister_class(TEXT_IO_PT_Panel)
    bpy.utils.unregister_class(SimpleOperator)


if __name__ == "__main__":
    register()