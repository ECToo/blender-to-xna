# Method #

There was a working method to export from Blender 2.49b to XNA 3.1 but that does not work for XNA 4.0 unless you use an XNA 3.1 application to create the files for use in XNA 4.0.

As files created using the XNA 3.1 FBX importer still work with XNA 4.0 I decided to compare the file outputs to see what has changed.

As the files are in a different order it was necessary to scan the files side by side.

# Results #

In the new version:

> - the armature Skeleton has been deliberately changed to be the root and removed the unnecessary Blend\_Root

> Model:

**- The meshes includes Edges, not present in the old FBX file (TODO: remove this)
> Jacket-Obj, Body-Obj etc.**

**- The meshes includes Smoothing, not present in the old FBX file (TODO: remove this from several sections)**

> - The layerElementMatrerials of the Body-Obj are different but similar.

> - The Limb's are now called LimbNode.  This was a deliberate change but it might be significant

> - The Limbs are not listed in the same order.

> The new FBX file lists the LimbNodes in armature order, the old one appears to be random.

> - Rounding is slightly difference.  In some cases in the old file the scale was not quite 1.0 but is in the new file

> - The Model Model::R-Collar in both files looks identical!

> Material:

> - The materials in the new file have been given unique names by tagging on the image file name to the end of the mesh name

> - Some of the colour values are slightly different

> Video:

> - Looks the same

> Texture:

> - Looks the same

> Deformer:

> - Listed in a different order (similar to the order the limbs are listed in the model)

> - The data looks the same

> Pose: "Pose::BIND\_POSES"

> - Listed in a different order

> - The new one includes an Identity matrix for the meshes but the old one does not include the meshes at all

> - The poses look the same (checked several including Waist and L-Collar)

**- At the end the GlobalSettings are different.**

> Property: "UnitScaleFactor", "double", "",100 in the old it is Property: "UnitScaleFactor", "double", "",1

> Relations:

> - Deliberately changed all the Limbs to LimbNodes

> - Everything else looks the same

> Connections:

> - Deliberately changed the Meshes to connect to the scene not to the armature

> - The list is in a different order

> - Some slight name changes as mentioned above but the links appear the same

> Takes:

> - The new one starts with Patrol2 the old one starts with Stand

> - The new one had the filename changed to Patrol2.tak and the old one keeps Default\_Take.tak

> Version 5 settings

> - Look identical

## Final Fix ##

The trouble with scanning by eye is it is easy to miss something.  When I was looking for something else I came across a difference I had not noticed before.

The Object for the armature was set as a 'Null' but the sample dude.fbx had this as a 'LimbNode'.  Changing that fixed the animations!