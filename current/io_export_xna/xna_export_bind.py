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
# - This Bind pose is only the individual bones not the cumulative pose
# - The floating point values in XNA Matrices are only to 7 decimal places
# --------------------------------------------------------------------------

# This script uses spaces for indents NOT tabs.
# Remember that there is a scripting console built in to Blender 2.5x
# See also: Help -> Operator Cheat Sheet from within Blender 2.5x

# --------------------------------------------------------------------------
# * Tasks *
# --------------------------------------------------------------------------
# Try:
#   from: 
#       http://www.sfr-fresh.com/linux/misc/blender-2.49-linux-glibc236-py26-i386.tar.gz:a/blender-2.49-linux-glibc236-py26-i386/.blender/scripts/bpymodules/colladaImEx/translator.py
#   bindMatrix = Matrix(bBone.matrix["ARMATURESPACE"]).resize4x4().transpose()
#   I don't think it needs the transpose bit
#   or
#   bindMatrix = Matrix(bArmature.bones[vertexGroupName].matrix['ARMATURESPACE']).transpose()
#   bindMatrix = Matrix(bMeshObject.matrix).transpose() * bindMatrix
# See also:
#   http://www.blender.org/documentation/250PythonDoc/bpy.types.Armature.html?highlight=armature#bpy.types.Armature
#   look at, pose_position['REST']
#   That does not work


# Descriptions
__author__ = ["John C Brown"]
__version__ = '1.0'
__bpydoc__ = """\
This script exports the bind pose to a file for analysis.

Usage:

Execute this script from the "File->Export" menu.

"""

import bpy
from mathutils import Matrix

IdentityMatrix = Matrix([1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1])   # Identity

class bind_bone:
    def __init__(self):
        self.Name = ""
        self.Bind_Matrix = Matrix()   # Identity

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
    

def export_bind(filepath, formatType):

    print ("Export the bind pose to file: {0}".format(filepath))
    
    
    # Store each bone transform as a separate line
    results = []
    # Number of bones
    boneCount = 0

    # Get the armature (hopefully only one)
    for arm_obj in bpy.context.scene.objects:
        if arm_obj.type == 'ARMATURE':
        
            print ("Armature: {0}".format(arm_obj.name))

            # Set to the REST pose
            #arm_obj.pose_position['REST']  # does not work
            
            # The pose bones in the armature store the rotations etc. for the animations
            # They also store a link back to the orignal bone to get its rotation etc.
            # http://www.blender.org/documentation/250PythonDoc/bpy.types.PoseBone.html
            poseBones = arm_obj.pose.bones

            # This counts all the bones in the armature
            boneCount = len(poseBones)

            # Calculate the bind pose
            bindPose = calc_bind_pose(arm_obj)
            print ("Number of bones in the bind pose: {0}".format(len(bindPose.binds)))
            
            for poseBone in poseBones:
                bone_obj = poseBone.bone
                parent_obj = poseBone.parent
            
                parentName = ""
                #print ("Bone name: {0}".format(bone_obj.name))
                if parent_obj:
                    parentName = parent_obj.bone.name
                else:
                    parentName = "root"
            
                # Save the local matrix
                boneMatrix = Matrix(bone_obj.matrix_local)
                # This should be the position relative to the object origin
                # http://www.blender.org/documentation/250PythonDoc/bpy.types.Bone.html
                # Split in to four rows just because it is tidier to read and therefore easier to debug
                # Format properties: http://www.python.org/dev/peps/pep-3101/
                # e.g. {0:.0f} displays a floating point number with a fixed size with 0 decimal places
                # if the f for fixed is omitted then small numbers are displayed using the exponential 0.000-E7 notation
                if formatType == 2:
                    # Calculate the result as the sum of the parent matrices
                    boneMatrix = bindPose.get(poseBone.bone.name)
                elif formatType == 3:
                    # Use the rest pose
                    #boneMatrix = bone_obj.matrix_local * Matrix(poseBone.matrix_local).invert()
                    boneMatrix = Matrix(bone_obj.matrix['ARMATURESPACE']).resize4x4()
                rowOne = "{0} {1} {2} {3}".format(boneMatrix[0][0], boneMatrix[0][1], boneMatrix[0][2], boneMatrix[0][3])
                rowTwo = "{0} {1} {2} {3}".format(boneMatrix[1][0], boneMatrix[1][1], boneMatrix[1][2], boneMatrix[1][3])
                rowThree = "{0} {1} {2} {3}".format(boneMatrix[2][0], boneMatrix[2][1], boneMatrix[2][2], boneMatrix[2][3])
                rowFour = "{0} {1} {2} {3}".format(boneMatrix[3][0], boneMatrix[3][1], boneMatrix[3][2], boneMatrix[3][3])
                resultFrame = "{0} [ {1} ] {2} {3} {4} {5}".format(bone_obj.name, parentName, rowOne, rowTwo, rowThree, rowFour)
                #resultFrame = "{0} | {1} {2} {3} {4}".format(bone_obj.name, rowOne, rowTwo, rowThree, rowFour)
                results.append(resultFrame)
            # Repeat for each bone

            # write the frames to a file
            file = open(filepath, "w")
            file.write("Bone count: {0}\n".format(boneCount))
            if formatType == 2:
                file.write("Bone [ Parent] Cumulative with parent matrices relative to the armature: {0}\n".format(arm_obj.name))
            else:
                file.write("Bone [ Parent] Absolute local matrix relative to the armature: {0}\n".format(arm_obj.name))
                #file.write("Bone | Local matrix relative to the armature: {0}\n".format(arm_obj.name))
            file.write("======================================================================================\n")
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
    format_type = IntProperty(name="Type", description="Type 1 = Absolute Matrix, Type 2 = Cumulative from parents Matrix, Type 3 = Rest pose", default=3, min=1, max=3)

    
    def execute(self, context):
        export_bind(self.filepath, self.format_type)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.add_fileselect(self)
        return {'RUNNING_MODAL'}

# package manages registering (__init__.py)
