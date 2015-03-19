# Process #

In the process of trying to rotate the animations I stumbled across a difference in the FBX file format that I had not noticed.  It was the same in the Blender 2.4x version of the FBX exporter but different in the sample FBX file I was comparing them to.

I changed the armature from being a 'Null' to being a 'LimbNode' object.  That simple change fixed everything.

The FBX SDK importer used for XNA still requires the animations to be in separate FBX files but that suits me anyway.  Shawn Hargreaves shows a method of merging them in the XNA pipeline if that is your preference.

http://blogs.msdn.com/b/shawnhar/archive/2010/06/18/merging-animation-files.aspx

I need to tidy up the scripts to remove unnecessary code and confusing UI options.
[Revision 75](https://code.google.com/p/blender-to-xna/source/detail?r=75) works but the code and UI are untidy anything newer than that will be neater.