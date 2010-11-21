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
# - Work out the file name based on the action name (if necessary)
#     Add the action name as a suffix to the filename (default)
#       Action as a filename suffix (filename-action.clip)
# - Once the animations work
#   - Round floating point number to 7 or 8 decimal places which should be acurate 
#       enough for our needs (perhaps try as low as 6 decimal places)
#       Try {0:9f} to have a field size of 9 rather than simply 8 decimal places
# Done - Change the importer for XNA to accept bone names and convert to their index
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

# --------------------------------------------------------------------------
# Links
# --------------------------------------------------------------------------
# Export keyframe calculation
# http://stackoverflow.com/questions/1273588/exporting-keyframes-in-blender-python
# The channel data should be applied on top of the bind pose matrix.
# The complete formula is the following:
# Mr = Ms * B0*P0 * B1*P1 ... Bn*Pn
# where:
# Mr = result matrix for a bone 'n'
# Ms = skeleton->world matrix
# Bi = bind pose matrix for bone 'i'
# Pi = pose actual matrix constructed from stored channels (that you are exporting)
# 'n-1' is a parent bone for 'n', 'n-2' is parent of 'n-1', ... , '0' is a parent of '1'
#
# Old but useful information on how the bine pose is stored
# http://www.blender.org/forum/viewtopic.php?p=49096&highlight=&sid=164bbb6e5435d5a9cbe22dfa2ed91243
#
# Useful discussion about bind pose and inverse bind pose matrices
# http://www.gamedev.net/community/forums/topic.asp?topic_id=571044
#
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
from mathutils import Matrix

IdentityMatrix = Matrix([1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1])   # Identity

# Remove if not used after testing
class bind_bone:
    def __init__(self):
        self.Name = ""
        self.Bind_Matrix = Matrix()   # Identity

# Remove if not used after testing
class bind_bones:
    def __init__(self):
        self.binds = []
    
    def addpose(self, name, bind_matrix):
        bBone = bind_bone()
        bBone.Name = name
        bBone.Bind_Matrix = bind_matrix
        self.binds.append(bBone)
        
    def get(self, name):
        for bBone in self.binds:
            if bBone.Name == name:
                return bBone.Bind_Matrix
        #return Matrix(IdentityMatrix)

# Remove if not used after testing
# Calculate the bind pose
# I don't think this works!!!!
def calc_bind_pose(arm_obj):
    
    binds = bind_bones()
    poseBones = arm_obj.pose.bones
    
    for poseBone in poseBones:
        matrix_bind = Matrix()
        if poseBone.parent:
            # add the local transformation to the cumulative of the parents
            parent_matrix = Matrix(binds.get(poseBone.parent.bone.name))
            matrix_bind = parent_matrix * poseBone.bone.matrix_local
            #print("{0} -> Parent: {1}".format(poseBone.bone.name, poseBone.parent.bone.name))
            binds.addpose(poseBone.bone.name, matrix_bind)
        else:
            parent_matrix = Matrix(IdentityMatrix)
            matrix_bind = parent_matrix * poseBone.bone.matrix_local
            #print("{0} -> Parent: root".format(poseBone.bone.name))
            binds.addpose(poseBone.bone.name, matrix_bind)
        
    # Loop pose bones
    return binds
    
# Format type is used while testing to output different information
def export_action(filepath, framesPerSecond, allActions, formatType):

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
    
    # Get the armature (hopefully only one)
    for arm_obj in bpy.context.scene.objects:
        if arm_obj.type == 'ARMATURE':
        
            print ("Armature: {0}".format(arm_obj.name))
            
            # get the current action
            if arm_obj.animation_data:
                if not currentAction:
                    currentAction =	arm_obj.animation_data.action

            # http://www.blender.org/documentation/250PythonDoc/bpy.types.Action.html
            if currentAction:
                print ("Action: {0}".format(currentAction.name))
                frameStart = int(currentAction.frame_range[0])
                frameEnd = int(currentAction.frame_range[1])
                frameCount = int(frameEnd - frameStart + 1)
                print ("Frame range from {0} to {1}".format(frameStart, frameEnd))
                # Calculate the total length of the animation loop
                totalClipTime = round((frameTime * (frameCount - 1)), 0)
                # This counts all the bones in the armature
                boneCount = len(arm_obj.pose.bones)
                print ("Number of bones: {0}".format(boneCount))
                print ("Total clip duration (ticks): {0:.0f}".format(totalClipTime))
                
                # Calculate the bind pose (Remove if not used after testing)
                bindPose = calc_bind_pose(arm_obj)
                print ("Number of bones in the bind pose: {0}".format(len(bindPose.binds)))
        
                # Loop through all the frames starting with the first one in the selected action
                # This gets every frame including those blended from inserted frames
                for frameID in range(0, frameCount):
                    # Set the current frame in the current action
                    # This sets the armature in to this frames pose
                    bpy.context.scene.frame_set(frameID + frameStart)
                    
                    # Calculate the frame start time
                    thisFrameTime = round(frameID * frameTime, 0)
                    
                    # Get every pose bone in the frame 
                    # the pose bones in the armature store the rotations etc. for the animations
                    # http://www.blender.org/documentation/250PythonDoc/bpy.types.PoseBone.html
                    # poseBones = arm_obj.pose.bones, returns all the bones ideally we would like a function that only
                    # returns the bones used in this action
                    poseBones = arm_obj.pose.bones
                    # The bones might not be sorted or indexed the way we need them so we will use the
                    # bone names and index and sort them when imported in to XNA
                    # The pose bone is not a bone but contains a link to the bone it is associated with.
                    # poseBones[i].bone
                    # The pose bones contain the rotation, location and scale and other settings in various formats
                    # the one we are most likely to need is .matrix_local (but this is still only beta in the 2.5x API)
                    # matrix_local is a 4x4 matrix.
                    for poseBone in poseBones:
                        # Save the local matrix
                        # Separate matrix variable for use during testing this script
                        boneMatrix = Matrix(poseBone.matrix_local)
                        # Split in to four rows just because it is tidier to read and therefore easier to debug
                        # Format properties: http://www.python.org/dev/peps/pep-3101/
                        # e.g. {0:.0f} displays a floating point number with a fixed size with 0 decimal places
                        # if the f for fixed is omitted then small numbers are displayed using the exponential 0.000-E7 notation
                        
                        # Remove the types when the correct method is found
                        if formatType == 2:
                            # The bind pose is local matrix of the bone associated with the pose bone
                            # Probably needs to be the cumulative of all the parent matrices
                            #       Add a calculation to work out the bind pose of each bone
                            #boneMatrix = boneMatrix * poseBone.bone.matrix_local
                            boneMatrix = boneMatrix * bindPose.get(poseBone.bone.name)
                        elif formatType == 3:
                            # Deliberate mistake with the sum reversed just used for testing
                            boneMatrix = poseBone.bone.matrix_local * boneMatrix
                        elif formatType == 4:
                            # Bind pose only used for testing
                            #boneMatrix = Matrix(poseBone.bone.matrix_local)
                            boneMatrix = bindPose.get(poseBone.bone.name)
                        rowOne = "{0} {1} {2} {3}".format(boneMatrix[0][0], boneMatrix[0][1], boneMatrix[0][2], boneMatrix[0][3])
                        rowTwo = "{0} {1} {2} {3}".format(boneMatrix[1][0], boneMatrix[1][1], boneMatrix[1][2], boneMatrix[1][3])
                        rowThree = "{0} {1} {2} {3}".format(boneMatrix[2][0], boneMatrix[2][1], boneMatrix[2][2], boneMatrix[2][3])
                        rowFour = "{0} {1} {2} {3}".format(boneMatrix[3][0], boneMatrix[3][1], boneMatrix[3][2], boneMatrix[3][3])
                        # Bone name, frame time and the transform matrix
                        resultFrame = "{0} {1:.0f}|{2} {3} {4} {5}".format(poseBone.bone.name, thisFrameTime, rowOne, rowTwo, rowThree, rowFour)
                        keyframes.append(resultFrame)
                        #print (resultFrame)

                # write the frames to a file
                file = open(filepath, "w")
                # The file format type for use by an importer
                file.write("{0}\n".format(formatType))
                # The bone count to check compatibility
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
class ActionExporter(bpy.types.Operator):
    '''Save actions compatible with XNA'''
    bl_idname = "xna_export_action.action"
    bl_label = "XNA Export Actions"

    filename_ext = ".action"
    
    # User interface
    # http://www.blender.org/documentation/250PythonDoc/bpy.props.html
    # This is very similar to the ExportHelper class in io_utils.py in the user folder .../2.55/scripts/modules 
    filepath = StringProperty(name="File Path", description="Filepath used for exporting the file", maxlen= 1024, default= "", subtype='FILE_PATH')
    check_existing = BoolProperty(name="Check Existing", description="Check and warn on overwriting existing files", default=True, options={'HIDDEN'})

    all_actions = BoolProperty(name="All Actions", description="No choice this only Exports the current action", default=False)
    frame_rate = IntProperty(name="Frames per second", description="The frame speed the animations are created for", default=60, min=1, max=960)
    format_type = IntProperty(name="Type", description="Type 1 = Matrix only, Type 2 = Matrix and bind pose, Type 3 = Deliberate mistake, Type 4 = Bind pose only", default=1, min=1, max=4)

    def execute(self, context):
        export_action(self.filepath, self.frame_rate, self.all_actions, self.format_type)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.add_fileselect(self)
        return {'RUNNING_MODAL'}

# package manages registering (__init__.py)
