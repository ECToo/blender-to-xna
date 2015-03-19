# Unified FBX Exporter #

Submitted patch #28118 29 July 2011

## Notes ##

  * The armature must be a Limb.
  * Limb and LimbNode do the same thing as far as I can tell.
  * The armature must be parented to the scene.
  * The first bone must be parented to the armature.
  * Linear or curve L or c,n make no difference to the output.
  * The calculation of the Rotation (TX\_CHAN == 'R') of the takes makes no difference.
  * I don't think the armature needs to be included as a bone in the animations because it always has a rotation of zero but I can't work out how to exclude it in the script!
  * The order of the connections does not matter although I would always want the bones in order just in case.


## List of Changes ##

  * Added warning about lone edges
  * Excludes lone edges from XNA output only
  * Added option to only output animations
  * Option to exclude the Default\_Take.tak name
  * Use the action name for the .tak filename
  * Added more descriptive instructions to the existing options
  * Added validation for XNA options to the UI
  * Added option to use the same folder for textures as the fbx is in
  * Output the selected action with its own name instead of Default\_Take
  * Removed all rotations
  * Bones return their own matrix in object\_tx()
  * Made the Armature a Limb