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
    "location": "File > Export > XNA Keyframes ",
    "description": "Export XNA Keyframes (.action format)",
    "warning": "",
    "wiki_url": "http://code.google.com/p/blender-to-xna/",
    "tracker_url": "http://code.google.com/p/blender-to-xna/",
    "category": "Import/Export"}

import bpy

# Not sure why this is used but something similar is present in most scripts
try:
    init_data
    # Add any classes here to reload if necessary
    reload(export_xna)
except:
    # Add any classes here to match above
    from io_export_xna import export_xna

init_data = True

'''
def menu_import(self, context):
    from io_export_xna import import_xna
    self.layout.operator(import_xna.XNAImporter.bl_idname, text="XNA Keyframes (.clip)").filepath = "*.clip"
'''

# Add each additional script in a simlar block to this
def menu_export(self, context):
    from io_export_xna import export_xna
    import os
    default_path = os.path.splitext(bpy.data.filepath)[0] + ".action"
    self.layout.operator(export_xna.XNAExporter.bl_idname, text="XNA Keyframes (.action)").filepath = default_path

# Add references to all scripts invoked by this class
def register():
    #bpy.types.INFO_MT_file_import.append(menu_import)
    bpy.types.INFO_MT_file_export.append(menu_export)

# Add references to all scripts invoked by this class
def unregister():
    #bpy.types.INFO_MT_file_import.remove(menu_import)
    bpy.types.INFO_MT_file_export.remove(menu_export)

if __name__ == "__main__":
    register()
