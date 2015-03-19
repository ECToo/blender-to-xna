# Latest Instructions #

The most up to date instructions will be on the Blender Wiki page:

http://wiki.blender.org/index.php/Extensions:2.5/Py/Scripts/File_I-O/Blender-toXNA

# Summary #

The Autodesk FBX Importer shipped with XNA 4.0 can only load one animation in each FBX file.  These scripts are written taking that in to account.

- Export the Model Only as an FBX.

- Export each Blender action as an FBX animation in to separate files.

- Load the model in to XNA and merge the animations.  See Shawn Hargreaves blog on how to merge animations or use my TakeExtrator model viewer for testing.


# Details #

If you have followed the installation instructions you should have 3 new menu items on the Export menu in Blender.  _XNA FBX Model only, XNA FBX Animations only_ and _XNA FBX Animated Model._

The _XNA FBX Model only_ exports the model with armature (if present) but only in the rest pose.  No animations.  This produces the smallest file size compatible with being animated in XNA.

The _XNA FBX Animations only_ option can be used to export each animation one at a time.  In pose mode in Blender select whichever action you want to export.  Then select the _Export -> XNA FBX Animations only_ from the menu and save that selected action.  Repeat selecting an action and exporting it for each animation you want to use in XNA.  This option produces a much smaller FBX file size because it does not contain any of the model data.

The _XNA FBX Animated Model_ option produces a complete FBX file with the model meshes and the animation take(s) all in one file.

# Resources #

Shawn Hargreaves blog on how to merge animations in XNA:

http://blogs.msdn.com/b/shawnhar/archive/2010/06/18/merging-animation-files.aspx

TakeExtractor project which lets you load a model and then load individual animations from FBX files.

http://code.google.com/p/take-extractor/