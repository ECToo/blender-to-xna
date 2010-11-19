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
# * Notes *
# --------------------------------------------------------------------------
# - The floating point values in XNA Matrices are only to 7 decimal places
# --------------------------------------------------------------------------

# This script uses spaces for indents NOT tabs.
# Remember that there is a scripting console built in to Blender 2.5x
# See also: Help -> Operator Cheat Sheet from within Blender 2.5x


# Descriptions
__author__ = ["John C Brown"]
__version__ = '1.0'
__bpydoc__ = """\
This script exports the bind pose to a file for analysis.

Usage:

Execute this script from the "File->Export" menu.

"""

import bpy
    

def export_bind(filepath):

    print ("Export the bind pose to file: {0}".format(filepath))
    
    
    # Store each bone transform as a separate line
    results = []
    # Number of bones
    boneCount = 0

    # Get the armature (hopefully only one)
    for arm_obj in bpy.context.scene.objects:
        if arm_obj.type == 'ARMATURE':
        
            print ("Armature: {0}".format(arm_obj.name))

            # The pose bones in the armature store the rotations etc. for the animations
            # They also store a link back to the orignal bone to get its rotation etc.
            # http://www.blender.org/documentation/250PythonDoc/bpy.types.PoseBone.html
            poseBones = arm_obj.pose.bones

            # This counts all the bones in the armature
            boneCount = len(poseBones)

            
            for poseBone in poseBones:
                bone_obj = poseBone.bone
                #parent_obj = poseBone.parent
            
                print ("Bone name: {0}".format(bone_obj.name))
                #print ("Parent name: {0}".format(parent_obj.name))
            
                # Save the local matrix
                # This should be the position relative to the object origin
                # http://www.blender.org/documentation/250PythonDoc/bpy.types.Bone.html
                # Split in to four rows just because it is tidier to read and therefore easier to debug
                # Format properties: http://www.python.org/dev/peps/pep-3101/
                # e.g. {0:.0f} displays a floating point number with a fixed size with 0 decimal places
                # if the f for fixed is omitted then small numbers are displayed using the exponential 0.000-E7 notation
                rowOne = "{0} {1} {2} {3}".format(bone_obj.matrix_local[0][0], bone_obj.matrix_local[0][1], bone_obj.matrix_local[0][2], bone_obj.matrix_local[0][3])
                rowTwo = "{0} {1} {2} {3}".format(bone_obj.matrix_local[1][0], bone_obj.matrix_local[1][1], bone_obj.matrix_local[1][2], bone_obj.matrix_local[1][3])
                rowThree = "{0} {1} {2} {3}".format(bone_obj.matrix_local[2][0], bone_obj.matrix_local[2][1], bone_obj.matrix_local[2][2], bone_obj.matrix_local[2][3])
                rowFour = "{0} {1} {2} {3}".format(bone_obj.matrix_local[3][0], bone_obj.matrix_local[3][1], bone_obj.matrix_local[3][2], bone_obj.matrix_local[3][3])
                #resultFrame = "{0} [ {1} ] {2} {3} {4} {5}".format(bone_obj.name, parent_obj.name, rowOne, rowTwo, rowThree, rowFour)
                resultFrame = "{0} | {1} {2} {3} {4}".format(bone_obj.name, rowOne, rowTwo, rowThree, rowFour)
                results.append(resultFrame)

                # write the frames to a file
                file = open(filepath, "w")
                file.write("Bone count: {0}\n".format(boneCount))
                #file.write("Bone [ Parent] Local matrix relative to the armature: {0}\n".format(arm_obj.name))
                file.write("Bone | Local matrix relative to the armature: {0}\n".format(arm_obj.name))
                file.write("================================================================================\n")
                for item in results:
                    file.write("{0}\n".format(item))
                file.close()
                print("Finished the bind pose for armature: {0}".format(arm_obj.name))
        
    # Repeat for each armature
    print("** Finished exporting **")

from bpy.props import *

# Starts here
# Display the user interface
class BindPoseExporter(bpy.types.Operator):
    '''Save the bind pose to a file'''
    bl_idname = "xna_export_bind.pose"
    bl_label = "XNA Export Bind Pose"

    filename_ext = ".pose"
    
    # User interface
    # http://www.blender.org/documentation/250PythonDoc/bpy.props.html
    # This is very similar to the ExportHelper class in io_utils.py in the user folder .../2.55/scripts/modules 
    filepath = StringProperty(name="File Path", description="Filepath used for exporting the file", maxlen= 1024, default= "", subtype='FILE_PATH')
    check_existing = BoolProperty(name="Check Existing", description="Check and warn on overwriting existing files", default=True, options={'HIDDEN'})

    #all_actions = BoolProperty(name="All Actions", description="No choice this only Exports the current action", default=False)
    #frame_rate = IntProperty(name="Frames per second", description="The frame speed the animations are created for", default=60, min=1, max=960)

    def execute(self, context):
        export_bind(self.filepath)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.add_fileselect(self)
        return {'RUNNING_MODAL'}

# package manages registering (__init__.py)
