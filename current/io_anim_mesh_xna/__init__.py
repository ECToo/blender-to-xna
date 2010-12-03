bl_addon_info = {
    "name": "Blender to XNA",
    "author": "John C Brown, JCBDigger (@MistyManor)",
    "version": (1,0),
    "blender": (2, 5, 5),
    "api": 32738,
    "location": "File > Export > FBX for XNA",
    "description": "Export the model and animations for use in XNA",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.5/Py/Scripts/File_I-O/Blender-toXNA",
    "tracker_url": "https://projects.blender.org/tracker/index.php?func=detail&aid=25013&group_id=153&atid=467",
    "category": "Import/Export"}

# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See the GNU General Public License on the GNU web site for full
# details: http://www.gnu.org/licenses/gpl.html
#
# ***** END GPL LICENCE BLOCK *****

# Blender to XNA

# Project Page:
# http://wiki.blender.org/index.php/Extensions:2.5/Py/Scripts/File_I-O/Blender-toXNA

# This script uses spaces for indents NOT tabs.


# To support reload properly, try to access a package var, if it's there, reload everything
if "bpy" in locals():
    import sys
    reload(sys.modules.get("io_export_xna.xna_fbx_export", sys))

import bpy

# Add each additional script in a simlar block to this
def menu_export_fbx_model(self, context):
    from io_export_xna import xna_fbx_export
    import os
    default_path = os.path.splitext(bpy.data.filepath)[0] + ".fbx"
    self.layout.operator(xna_fbx_export.ExportFBXmodel.bl_idname, text="XNA FBX Model only (.fbx)").filepath = default_path

def menu_export_fbx_takes(self, context):
    from io_export_xna import xna_fbx_export
    import os
    # get the current action name
    currentAction = ""
    for arm_obj in bpy.context.scene.objects:
        if arm_obj.type == 'ARMATURE':
            if arm_obj.animation_data:
                if currentAction == "":
                    currentAction = arm_obj.animation_data.action.name
    
    default_path = os.path.splitext(bpy.data.filepath)[0] + "-" + currentAction + ".fbx"
    self.layout.operator(xna_fbx_export.ExportFBXtakes.bl_idname, text="XNA FBX Animations only (.fbx)").filepath = default_path
    
def menu_export_fbx_animated(self, context):
    from io_export_xna import xna_fbx_export
    import os
    default_path = os.path.splitext(bpy.data.filepath)[0] + ".fbx"
    self.layout.operator(xna_fbx_export.ExportFBXanimated.bl_idname, text="XNA FBX Animated Model (.fbx)").filepath = default_path


# Add references to all scripts invoked by this class
def register():
    bpy.types.INFO_MT_file_export.append(menu_export_fbx_animated)
    bpy.types.INFO_MT_file_export.append(menu_export_fbx_model)
    bpy.types.INFO_MT_file_export.append(menu_export_fbx_takes)

# Add references to all scripts invoked by this class
def unregister():
    bpy.types.INFO_MT_file_export.remove(menu_export_fbx_animated)
    bpy.types.INFO_MT_file_export.remove(menu_export_fbx_model)
    bpy.types.INFO_MT_file_export.remove(menu_export_fbx_takes)

if __name__ == "__main__":
    register()
