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
# * File format *
# --------------------------------------------------------------------------
# First line:
# Number of bones in the armature (space) duration of the animation loop
# One line for each keyframe bone transform:
# BoneID (space) FrameTime |(pipe) Transform matrix (space separated numbers)
# --------------------------------------------------------------------------
# ** Limitations **
# --------------------------------------------------------------------------
# - Can only export the currently selected action
# --------------------------------------------------------------------------


# This script uses spaces for indents NOT tabs.
# Remember that there is a scripting console built in to Blender 2.5x
# See: Help -> Operator Cheat Sheet from within Blender 2.5x

# --------------------------------------------------------------------------
# *** TASKS ***
# --------------------------------------------------------------------------
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
    

def export_xna(filepath, currentAction):

    # store each keyframe bone transform as a separate line
    # File format:
    # BoneID FrameTime | Transform matrix
    keyframes = []
    # Number of bones
    boneCount = 0

    currentAction = None
    
    # Currently selected (context) action
    KeyframeCount = bpy.context.scene.frame_end - bpy.context.scene.frame_start + 1

    # Get the armature (hopefully only one)
    for arm_obj in bpy.context.scene.objects:
        if arm_obj.type == 'ARMATURE':
        
            print ('Armature: %s' % arm_obj.name)
            
            # get the current action
            if arm_obj.animation_data:
                if not currentAction:
                    currentAction =	arm_obj.animation_data.action

            if currentAction:
            
                print ('Current Action: %s' % currentAction.name)
            
                boneCount = len(arm_obj.pose.bones)
        
                # Loop through all the frames starting with the first one in the selected action
                for frameID in range(0, KeyframeCount):
                    # I think this sets the current frame
                    bpy.context.scene.frame_set(frameID + bpy.context.scene.frame_start)
                    
                    # Try getting every bone in the frame 
                    # bpy.context.scene.frame.bones (or something like that)
                    
                    # for bone in bpy.context.scene.frame.bones:
                    
                        # bone.matrix_lo
                
                    keyframes.append(stuff)

                # write the frames to a file
                file = open(filepath, "w")
                file.write('%s \n' % boneCount)
                for keyframe in keyframes:
                    file.write(keyframe)
                file.close()
        
    # Repeat for each armature

from bpy.props import *

# Starts here
class XNAExporter(bpy.types.Operator):
    '''Save XNA compatible animations'''
    bl_idname = "export_xna.clip"
    bl_label = "Export XNA animation clips"

    filepath = StringProperty(name="File Path", description="Filepath used for exporting the file", maxlen= 1024, default= "", subtype='FILE_PATH')
    check_existing = BoolProperty(name="Check Existing", description="Check and warn on overwriting existing files", default=True, options={'HIDDEN'})

    current_action = BoolProperty(name="Current Action", description="No choice this only Exports the current action", default=True)

    def execute(self, context):
        export_xna(self.filepath, self.current_action)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.add_fileselect(self)
        return {'RUNNING_MODAL'}

# package manages registering
