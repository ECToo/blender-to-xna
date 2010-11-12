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
# ** HISTORY **
# --------------------------------------------------------------------------
# JCBDigger (@MistyManor) http://games.DiscoverThat.co.uk
# After various attempts to get an FBX exporter to produce animations
# that work with XNA 4.0 this is an alternate solution using the keyframe
# format from the XNA skinning sample.
# --------------------------------------------------------------------------

# This script uses spaces for indents NOT tabs.

# --------------------------------------------------------------------------
# *** TASKS ***
# --------------------------------------------------------------------------
# - Remove all unnecessary code from the script I used as a starting point
# - Create the user interface
#     All actions or just the current action (default to current only)
#     Add the action name as a suffix to the filename (default)
#       Action as a filename suffix (filename-action.clip)
# - Work out the file name based on the action name (if necessary)
# - Check that there is only one armature
# - Check that the bones are all in that armature
# - Calculate how many bones are used in the armature
# - Calculate the total time of the animation
# - Loop through all keyframes in the animation
# - Convert the time to be the same as used by XNA
# - Convert to a matrix
#     May also have an option for separate Scale, rotation and location
#     depending on how blender stores the keyframes
#       Matrix or Quaternion output
# - Does Blender store just the keyframes or all the intermediate blended ones
#     Ideally we need all frames not just the keyframes
#       I think the DirectX exporter has a method for getting to all frames
# - Save it all to a text file
# --------------------------------------------------------------------------


# Descriptions
__author__ = ["John C Brown"]
__version__ = '1.0'
__bpydoc__ = """\
This script exports animation keyframes to a file format suitable for XNA.

The format is very simple being just the bone, the frame time and the 
Rotation, Location and scale of the transform.

Usage:

Execute this script from the "File->Export" menu.

"""

import bpy


def faceToTriangles(face):
    triangles = []
    if (len(face) == 4): #quad
        triangles.append( [ face[0], face[1], face[2] ] )
        triangles.append( [ face[2], face[3], face[0] ] )
    else:
        triangles.append(face)

    return triangles


def faceValues(face, mesh, matrix):
    fv = []
    for verti in face.vertices_raw:
        fv.append(matrix * mesh.vertices[verti].co)
    return fv


def faceToLine(face):
    line = ""
    for v in face:
        line += str(v[0]) + " " + str(v[1]) + " " + str(v[2]) + " "
    return line[:-1] + "\n"


def export_xna(filepath, applyMods, triangulate):
    faces = []
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            matrix = obj.matrix_world

            if (applyMods):
                me = obj.create_mesh(bpy.context.scene, True, "PREVIEW")
            else:
                me = obj.data

            for face in me.faces:
                fv = faceValues(face, me, matrix)
                if triangulate:
                    faces.extend(faceToTriangles(fv))
                else:
                    faces.append(fv)

    # write the faces to a file
    file = open(filepath, "w")
    for face in faces:
        file.write(faceToLine(face))
    file.close()


from bpy.props import *

# Starts here
class XNAExporter(bpy.types.Operator):
    '''Save XNA compatible animations'''
    bl_idname = "export_xna.clip"
    bl_label = "Export XNA animation clips"

    filepath = StringProperty(name="File Path", description="Filepath used for exporting the file", maxlen= 1024, default= "", subtype='FILE_PATH')
    check_existing = BoolProperty(name="Check Existing", description="Check and warn on overwriting existing files", default=True, options={'HIDDEN'})

    apply_modifiers = BoolProperty(name="Apply Modifiers", description="Use transformed mesh data from each object", default=True)
    triangulate = BoolProperty(name="Triangulate", description="Triangulate quads.", default=True)

    def execute(self, context):
        export_xna(self.filepath, self.apply_modifiers, self.triangulate)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.add_fileselect(self)
        return {'RUNNING_MODAL'}

# package manages registering
