# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {
    "name": "Autodesk FBX format for XNA",
    "author": "John C Brown, JCBDigger (@MistyManor)",
    "blender": (2, 5, 9),
    "api": 38691,
    "location": "File > Import-Export",
    "description": "Export FBX models and animations for use in XNA",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.5/Py/"\
        "Scripts/Import-Export/Blender-toXNA",
    "tracker_url": "https://projects.blender.org/tracker/index.php?"\
        "func=detail&aid=25013",
    "category": "Import-Export"}

# This is the same as the OFFICIAL version but with the defaults set for XNA
    
# To support reload properly, try to access a package var, if it's there, reload everything
if "bpy" in locals():
    import imp
    if "export_fbx" in locals():
        imp.reload(export_fbx)


import bpy
from bpy.props import StringProperty, BoolProperty, FloatProperty, EnumProperty

from bpy_extras.io_utils import (ExportHelper, 
                                 path_reference_mode,
                                 axis_conversion,
                                 axis_conversion_ensure,
                                 )

# XNA can only use one take per file so there will be a lot of FBX files for the same model (JCB)
# Rename the file based on the action name (JCB)
def add_action_to_filepath(self):
    import os
    if self.ANIM_ENABLE and self.takes_only and not self.ANIM_ACTION_ALL:
        existing_name = self.filepath
        # get the current action name
        currentAction = ""
        for arm_obj in bpy.context.scene.objects:
            if arm_obj.type == 'ARMATURE':
                if arm_obj.animation_data:
                    if currentAction == "":
                        currentAction = arm_obj.animation_data.action.name
        # use the action name as a suffix to the existing blend filename.
        self.filepath = os.path.splitext(bpy.data.filepath)[0] + "-" + currentAction + ".fbx"
        if existing_name != self.filepath:
            return True
        else:
            return False
    else:
        return False
             
# Validate that the options are compatible with XNA (JCB)
def validate_xna_options(self):
    if self.xna_validate:
        changed = False
        if self.enable_rotation or not self.armature_limb:
            changed = True
            self.enable_rotation = False
            self.armature_limb = True
        if self.global_scale != 1.0 or self.mesh_smooth_type != 'OFF':
            changed = True
            self.global_scale = 1.0
            self.mesh_smooth_type = 'OFF'
        if not self.all_same_folder or self.use_default_take or self.ANIM_OPTIMIZE or self.include_edges:
            changed = True
            self.all_same_folder = True
            self.use_default_take = False
            self.ANIM_OPTIMIZE = False
            self.include_edges = False
        if 'CAMERA' in self.object_types or 'LAMP' in self.object_types or 'EMPTY' in self.object_types:
            changed = True
            # I could not get .remove to work
            #self.object_types.remove('CAMERA')
            self.object_types={'ARMATURE', 'MESH'}
        return changed
    else:
        return False

             
class ExportFBX(bpy.types.Operator, ExportHelper):
    '''Selection to an ASCII Autodesk FBX'''
    bl_idname = "export_scene.fbx"
    bl_label = "Export FBX"
    bl_options = {'PRESET'}

    filename_ext = ".fbx"
    filter_glob = StringProperty(default="*.fbx", options={'HIDDEN'})

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.

    use_selection = BoolProperty(name="Selected Objects", description="Export selected objects on visible layers", default=False)
    # XNA does not support scaled armatures (JCB)
    global_scale = FloatProperty(name="Scale", description="Scale all data. Some importers do not support scaled armatures!", min=0.01, max=1000.0, soft_min=0.01, soft_max=1000.0, default=1.0)
    # The armature rotation does not work for XNA and setting the global matrix to identity is not sufficient on its own (JCB)
    enable_rotation = BoolProperty(name="Enable Rotation", description="Must be on for rotation settings to be applied.", default=False)

    axis_forward = EnumProperty(
            name="Forward",
            description="Select the axis to be rotated to forwards then one of the other axes to be up.",
            items=(('X', "X Forward", ""),
                   ('Y', "Y Forward", ""),
                   ('Z', "Z Forward", ""),
                   ('-X', "-X Forward", ""),
                   ('-Y', "-Y Forward (Blender)", ""),
                   ('-Z', "-Z Forward", ""),
                   ),
            default='-Z',
            )

    axis_up = EnumProperty(
            name="Up",
            description="Must select the forward axis before selecting the up axis.",
            items=(('X', "X Up", ""),
                   ('Y', "Y Up", ""),
                   ('Z', "Z Up (Blender)", ""),
                   ('-X', "-X Up", ""),
                   ('-Y', "-Y Up", ""),
                   ('-Z', "-Z Up", ""),
                   ),
            default='Y',
            )

    object_types = EnumProperty(
            name="Object Types",
            options={'ENUM_FLAG'},
            items=(('EMPTY', "Empty", ""),
                   ('CAMERA', "Camera", ""),
                   ('LAMP', "Lamp", ""),
                   ('ARMATURE', "Armature", ""),
                   ('MESH', "Mesh", ""),
                   ),
            default={'ARMATURE', 'MESH'},
            )

    mesh_apply_modifiers = BoolProperty(name="Apply Modifiers", description="Apply modifiers to mesh objects", default=True)

    mesh_smooth_type = EnumProperty(
            name="Smoothing",
            items=(('OFF', "Off", "Don't write smoothing"),
                   ('FACE', "Face", "Write face smoothing"),
                   ('EDGE', "Edge", "Write edge smoothing"),
                   ),
            default='OFF',
            )


    # XNA does not use the edge information (JCB)
    include_edges = BoolProperty(name="Include Edges", description="Edges may not be necessary and can cause errors with some importers!", default=False)
#    EXP_MESH_HQ_NORMALS = BoolProperty(name="HQ Normals", description="Generate high quality normals", default=True)
    # armature animation
    ANIM_ENABLE = BoolProperty(name="Include Animation", description="Export keyframe animation", default=True)
    # XNA needs each animation in a separate FBX file but it does not need the model each time (JCB)
    takes_only = BoolProperty(name="Only Animations", description="Export will not include any meshes", default=False)
    ANIM_ACTION_ALL = BoolProperty(name="All Actions", description="Export all actions for armatures or just the currently selected action", default=False)
    ANIM_OPTIMIZE = BoolProperty(name="Optimize Keyframes", description="Remove double keyframes", default=False)
    ANIM_OPTIMIZE_PRECISSION = FloatProperty(name="Precision", description="Tolerence for comparing double keyframes (higher for greater accuracy)", min=1, max=16, soft_min=1, soft_max=16, default=6.0)
    # XNA needs different names for each take having the first one always called Default_Take is unhelpful (JCB)
    use_default_take = BoolProperty(name="Include Default_Take", description="Compatibility: Include an action called Default_Take", default=False)
    # XNA usually errors if the textures are not in the same folder as the FBX file (JCB)
    all_same_folder = BoolProperty(name="Same Folder", description="The FBX importer will expect the textures to be in the same folder as the FBX file.", default=True)
    # XNA requires the armature to be included as the root limb and that the first bone is parented to the armature limb! (JCB)
    armature_limb = BoolProperty(name="Armature Include As Bone", description="Compatibility: Include the armature object as the root bone for the skeleton.", default=True)
    # XNA - validation to avoid incompatible settings.  I will understand if this is not kept in the generic version. (JCB)
    # It would be nice to have this for XNA, UDK, Unity and Sunburn if others could provide the details. (JCB)
    xna_validate = BoolProperty(name="XNA Strict Options", description="Make sure options are compatible with Microsoft XNA", default=True)

    batch_mode = EnumProperty(
            name="Batch Mode",
            items=(('OFF', "Off", "Active scene to file"),
                   ('SCENE', "Scene", "Each scene as a file"),
                   ('GROUP', "Group", "Each group as a file"),
                   ),
            )

    BATCH_OWN_DIR = BoolProperty(name="Own Dir", description="Create a dir for each exported file", default=True)
    use_metadata = BoolProperty(name="Use Metadata", default=True, options={'HIDDEN'})

    path_mode = path_reference_mode

    @property
    def check_extension(self):
        return self.batch_mode == 'OFF'

    # I cannot find any description of how to use this method in the API documentation.  (JCB)
    # I have assumed that check() returns True if something has changed and False if nothing has changed? (JCB)
    def check(self, context):
        one = validate_xna_options(self)
        two = add_action_to_filepath(self)
        three = axis_conversion_ensure(self, "axis_forward", "axis_up")
        if one or two or three:
            return True
        else:
            return False

    def execute(self, context):
        from mathutils import Matrix
        if not self.filepath:
            raise Exception("filepath not set")

        # Armature rotation causes a mess in XNA there are also other changes in the main script to avoid rotation (JCB)
        global_matrix = Matrix()
        if self.enable_rotation:
            global_matrix[0][0] = global_matrix[1][1] = global_matrix[2][2] = self.global_scale
            global_matrix = global_matrix * axis_conversion(to_forward=self.axis_forward, to_up=self.axis_up).to_4x4()
        else:
            global_matrix[0][0] = global_matrix[1][1] = global_matrix[2][2] = self.global_scale
            global_matrix = global_matrix.to_4x4()
        
        keywords = self.as_keywords(ignore=("axis_forward", "axis_up", "global_scale", "check_existing", "filter_glob", "xna_validate"))
        keywords["global_matrix"] = global_matrix

        from . import export_fbx
        return export_fbx.save(self, context, **keywords)


def menu_func(self, context):
    self.layout.operator(ExportFBX.bl_idname, text="Autodesk FBX (.fbx)")


def register():
    bpy.utils.register_module(__name__)

    bpy.types.INFO_MT_file_export.append(menu_func)


def unregister():
    bpy.utils.unregister_module(__name__)

    bpy.types.INFO_MT_file_export.remove(menu_func)

if __name__ == "__main__":
    register()
