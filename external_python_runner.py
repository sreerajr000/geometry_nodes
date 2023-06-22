bl_info = {
    "name": "External Python Runner",
    "author": "Sreeraj Ramachandran",
    "version": (1, 0),
    "blender": (3, 4, 0),
    "location": "Geometry Node Editor > Header > Run Python Script",
    "description": "Run external Python scripts",
    "warning": "",
    "wiki_url": "",
    "category": "Development",
}

import bpy
import os

class ExternalScriptSettings(bpy.types.PropertyGroup):
    filepath: bpy.props.StringProperty(
        name="Filepath",
        subtype='FILE_PATH',
    )

class RunExternalPythonOperator(bpy.types.Operator):
    bl_idname = "object.run_external_python"
    bl_label = "Run Python Script"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        filename = context.scene.external_script_settings.filepath

        if os.path.isfile(filename):
            exec(compile(open(filename).read(), filename, 'exec'), {})
        else:
            self.report({'WARNING'}, f"No file found at path: {filename}")

        return {'FINISHED'}

def draw_func(self, context):
    layout = self.layout
    row = layout.row()
    row.prop(context.scene.external_script_settings, "filepath")
    row.operator(RunExternalPythonOperator.bl_idname, text="Run")

def register():
    bpy.utils.register_class(RunExternalPythonOperator)
    bpy.utils.register_class(ExternalScriptSettings)

    bpy.types.Scene.external_script_settings = bpy.props.PointerProperty(type=ExternalScriptSettings)
    bpy.types.NODE_HT_header.append(draw_func)

def unregister():
    bpy.utils.unregister_class(RunExternalPythonOperator)
    bpy.utils.unregister_class(ExternalScriptSettings)

    del bpy.types.Scene.external_script_settings
    bpy.types.NODE_HT_header.remove(draw_func)

if __name__ == "__main__":
    register()
