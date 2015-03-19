# Progress #

After lots of testing it appears that if the first (and only) pose saved in the FBX file is the bind pose (just one frame) then all the animations work as expected.

This is unexpected because there is a separate bind pose section in the FBX file but that appears to be ignored by XNA!

Now I need to work out how to create the bind pose in the script as a take!