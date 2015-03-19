## Initial Thoughts ##

This is a list of ideas that might make the FBX file compatible with XNA

By comparing a working FBX file (dude.fbx) with one exported from Blender the following ideas stand out:

Takes

These should be the same as in Blender 2.49b

Remove the ‘Default\_Take’ it is unnecessary and blocks the one allowed take

Deformer (Weights)

Have a quick check of these but if the model is not rotated these should be the same.

See the Transforms lines which might have rotate values.

Connections

Remove the ‘Blend\_Root’

Make ‘Skeleton’ (the name of the armature) the root

Connect the armature (Skeleton) to the scene

Check that the ‘Waist’ (first bone) is connected to the ‘skeleton’ (armature)

Connect all the meshes to the scene instead of to the armature (skeleton)


Relations

Change ‘Limb’ to ‘LimbNode’

Change the armature (skeleton) to be a ‘LimbNode’ instead of a null.

### Comments ###

The secondary items, Deformer, Connections and Relations have been done and tested. The resulting FBX still loads as a non-animated mesh.

Now need to work on the takes.
At the moment they load without complaint but the resulting animation is a contorted mess!

Having looked at several FBX files there is no need for any form of root object.  A valid model can be as simple as a single mesh connected to the scene.

Have eventually managed to find the settings to replicate the output from the Blender 2.4x version of the exporter.  May not be an exact match but close.

This is the starting point for trying to get the result to look right with XNA 4.


I am now looking at using my own format for animations and just using FBX for the mesh, bones and bone weights.


If I use the action format I have created with the FBX model exported from Blender v2.49b then the animations work.

It looks like the bones that are not directly connected head to tail cause problems with the new version of the FBX export and XNA.  Edit:  that is a red herring

Next plan is to compare in more detail the FBX files from v2.49b and try to make the new ones exactly the same.