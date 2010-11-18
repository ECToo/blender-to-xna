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
    "location": "File > Export > XNA Keyframes and XNA FBX model",
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
    reload(xna_export_action)
    reload(xna_export_fbx)
    reload(xna_export_bind)
except:
    # Add any classes here to match above
    from io_export_xna import xna_export_action
    from io_export_xna import xna_export_fbx
    from io_export_xna import xna_export_bind

init_data = True

# Add each additional script in a simlar block to this
def menu_export_action(self, context):
    from io_export_xna import xna_export_action
    import os
    default_path = os.path.splitext(bpy.data.filepath)[0] + ".action"
    self.layout.operator(xna_export_action.ActionExporter.bl_idname, text="XNA Keyframes (.action)").filepath = default_path

def menu_export_fbx(self, context):
    from io_export_xna import xna_export_fbx
    import os
    default_path = os.path.splitext(bpy.data.filepath)[0] + ".fbx"
    self.layout.operator(xna_export_fbx.FBXExporter.bl_idname, text="XNA FBX Model (.fbx)").filepath = default_path

def menu_export_bind(self, context):
    from io_export_xna import xna_export_bind
    import os
    default_path = os.path.splitext(bpy.data.filepath)[0] + ".pose"
    self.layout.operator(xna_export_bind.BindPoseExporter.bl_idname, text="XNA Bind Pose (.pose)").filepath = default_path

# Add references to all scripts invoked by this class
def register():
    bpy.types.INFO_MT_file_export.append(menu_export_action)
    bpy.types.INFO_MT_file_export.append(menu_export_fbx)
    bpy.types.INFO_MT_file_export.append(menu_export_bind)

# Add references to all scripts invoked by this class
def unregister():
    bpy.types.INFO_MT_file_export.remove(menu_export_action)
    bpy.types.INFO_MT_file_export.remove(menu_export_fbx)
    bpy.types.INFO_MT_file_export.remove(menu_export_bind)

if __name__ == "__main__":
    register()