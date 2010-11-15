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
# See also: Help -> Operator Cheat Sheet from within Blender 2.5x

# --------------------------------------------------------------------------
# *** TASKS ***
# --------------------------------------------------------------------------
# - Change the importer for XNA to accept bone names and convert to their index
# - Work out the file name based on the action name (if necessary)
#     Add the action name as a suffix to the filename (default)
#       Action as a filename suffix (filename-action.clip)
# - Once the animations work
#   - Round floating point number to 7 or 8 decimal places which should be acurate 
#       enough for our needs (perhaps try as low as 6 decimal places)
#       Try {0:9f} to have a field size of 9 rather than simply 8 decimal places
# Done - Create the user interface
# Does for all - Check that there is only one armature
# Done - Check that the bones are all in that armature
# Done - Loop through all keyframes in the animation
# Done - Calculate how many bones are used in the armature
# Done - Calculate the total time of the animation
# Done - Get the start time of each frame (calculated)
# Done - Convert the time to be the same as used by XNA (calculated)
# Done - (not necessary) Convert to a matrix
# Done - The method used gets all the intermedial blended frames not just the keyframes
# Done - Save it all to a text file
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
    

def export_xna(filepath, framesPerSecond, allActions):

    print ("Export animation(s) to file: {0}".format(filepath))
    
    # The frame times in XNA are measured in ticks (or something like that.)
    # There are 10,000,000 of them per second.
    # The output time per frame is rounded to the nearest integer e.g. round( time, 0 )
    # The individual frame time should be the floating point value for most 
    # accuracy but it is unlikely to make any noticable difference to the resulting animation
    frameTime = 10000000.0 / framesPerSecond
    
    # Store each keyframe bone transform as a separate line
    # File format:
    # BoneID FrameTime | Transform matrix
    keyframes = []
    # Number of bones
    boneCount = 0
    # At the moment this only exports the current animation
    currentAction = None
    
    # The start and end frame set within the action editor for playback
    # this is not what we want we need the frames in the current action
    keyFrameCount = bpy.context.scene.frame_end - bpy.context.scene.frame_start + 1
    # The time from the start to the end of the clip where it usually loops back to the start again
    totalClipTime = round((frameTime * (keyFrameCount - 1)), 0)

    # Get the armature (hopefully only one)
    for arm_obj in bpy.context.scene.objects:
        if arm_obj.type == 'ARMATURE':
        
            print ("Armature: {0}".format(arm_obj.name))
            
            # get the current action
            if arm_obj.animation_data:
                if not currentAction:
                    currentAction =	arm_obj.animation_data.action

            if currentAction:
                print ("Action: {0}".format(currentAction.name))
                
                print ("FCurve count: {0}".format(len(currentAction.fcurves)))
            
                boneCount = len(arm_obj.pose.bones)
                print ("Number of bones: {0}".format(boneCount))
                print ("Total clip duration (ticks): {0:.0f}".format(totalClipTime))
        
                # Loop through all the frames starting with the first one in the selected action
                # This gets every frame including those blended from inserted frames
                for frameID in range(0, keyFrameCount):
                    # Set the current frame in the current action
                    # This sets the armature in to this frames pose (I hope!)
                    bpy.context.scene.frame_set(frameID + bpy.context.scene.frame_start)
                    
                    # Calculate the frame start time
                    thisFrameTime = round(frameID * frameTime, 0)
                    
                    # Get every pose bone in the frame 
                    # the pose bones in the armature store the rotations etc. for the animations
                    # http://www.blender.org/documentation/250PythonDoc/bpy.types.PoseBone.html#bpy.types.PoseBone
                    poseBones = arm_obj.pose.bones
                    # The bones are unlikely to be sorted or indexed so we will use the
                    # bone names and index them later for use by XNA (or import and index them in XNA perhaps?)
                    # The pose bone is not a bone but contains a link to the bone it is associated with.
                    # poseBones[i].bone
                    # The pose bones contain the rotation, location and scale and other settings in various formats
                    # the one we are most likely to need is .matrix_local (but this is still only beta in the 2.5x API)
                    # matrix_local is a 4x4 matrix.
                    # TODO: is matrix_local relative to the parent bone or the inverse (e.g. the parent relative to the child)
                    for poseBone in poseBones:
                        # Save the local matrix
                        # Split in to four rows just because it is tidier to read and therefore easier to debug
                        # Format properties: http://www.python.org/dev/peps/pep-3101/
                        # e.g. {0:.0f} displays a floating point number with a fixed size with 0 decimal places
                        # if the f for fixed is omitted then small numbers are displayed using the exponential 0.000-E7 notation
                        rowOne = "{0} {1} {2} {3}".format(poseBone.matrix_local[0][0], poseBone.matrix_local[0][1], poseBone.matrix_local[0][2], poseBone.matrix_local[0][3])
                        rowTwo = "{0} {1} {2} {3}".format(poseBone.matrix_local[1][0], poseBone.matrix_local[1][1], poseBone.matrix_local[1][2], poseBone.matrix_local[1][3])
                        rowThree = "{0} {1} {2} {3}".format(poseBone.matrix_local[2][0], poseBone.matrix_local[2][1], poseBone.matrix_local[2][2], poseBone.matrix_local[2][3])
                        rowFour = "{0} {1} {2} {3}".format(poseBone.matrix_local[3][0], poseBone.matrix_local[3][1], poseBone.matrix_local[3][2], poseBone.matrix_local[3][3])
                        resultFrame = "{0} {1:.0f}|{2} {3} {4} {5}".format(poseBone.bone.name, thisFrameTime, rowOne, rowTwo, rowThree, rowFour)
                        keyframes.append(resultFrame)
                        #print (resultFrame)

                # write the frames to a file
                file = open(filepath, "w")
                file.write("{0} {1:.0f}\n".format(boneCount, totalClipTime))
                for keyframe in keyframes:
                    file.write("{0}\n".format(keyframe))
                file.close()
                print("Finished the action: {0}, for armature: {1}".format(currentAction.name, arm_obj.name))
        
    # Repeat for each armature
    print("** Finished exporting to XNA **")

from bpy.props import *

# Starts here
# Display the user interface
class XNAExporter(bpy.types.Operator):
    '''Save XNA compatible animations'''
    bl_idname = "export_xna.clip"
    bl_label = "Export XNA clips"

    # User interface
    # http://www.blender.org/documentation/250PythonDoc/bpy.props.html
    filepath = StringProperty(name="File Path", description="Filepath used for exporting the file", maxlen= 1024, default= "", subtype='FILE_PATH')
    check_existing = BoolProperty(name="Check Existing", description="Check and warn on overwriting existing files", default=True, options={'HIDDEN'})

    all_actions = BoolProperty(name="All Actions", description="No choice this only Exports the current action", default=False)
    frame_rate = IntProperty(name="Frames per second", description="The frame speed the animations are created for", default=60, min=1, max=960)

    def execute(self, context):
        export_xna(self.filepath, self.frame_rate, self.all_actions)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.add_fileselect(self)
        return {'RUNNING_MODAL'}

# package manages registering (__init__.py)
