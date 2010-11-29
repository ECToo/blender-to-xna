# --------------------------------------------------------------------------
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
# --------------------------------------------------------------------------
# Blender to XNA
# --------------------------------------------------------------------------
# Project Home:
# http://code.google.com/p/blender-to-xna/
# --------------------------------------------------------------------------

# This script uses spaces for indents NOT tabs.

bl_addon_info = {
    "name": "Blender to XNA",
    "author": "John C Brown, JCBDigger (@MistyManor)",
    "version": (1,0),
    "blender": (2, 5, 5),
    "api": 32738,
    "location": "File > Export > XNA FBX Animated Model",
    "description": "Export the model and animations for use in XNA",
    "warning": "",
    "wiki_url": "http://code.google.com/p/blender-to-xna/",
    "tracker_url": "http://code.google.com/p/blender-to-xna/",
    "category": "Import/Export"}

import bpy

# Not sure why this is used but something similar is present in most scripts
try:
    init_data
    # Add any classes here to reload if necessary
    reload(xna_fbx_export)
except:
    # Add any classes here to match above
    from io_export_xna import xna_fbx_export

init_data = True

# Add each additional script in a simlar block to this
def menu_export_fbx_model(self, context):
    from io_export_xna import xna_fbx_export
    import os
    default_path = os.path.splitext(bpy.data.filepath)[0] + ".fbx"
    self.layout.operator(xna_fbx_export.ExportFBXmodel.bl_idname, text="XNA FBX Model (.fbx)").filepath = default_path

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
    self.layout.operator(xna_fbx_export.ExportFBXtakes.bl_idname, text="XNA FBX Animations (.fbx)").filepath = default_path
    
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
