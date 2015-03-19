# Why is FBX a pain? #

It has taken me over a month to get an FBX exporter working with XNA.  My initial experiments to adjust the existing FBX exporter to work with XNA failed.  It was particularly difficult because the FBX file format is not documented.  The other problem was that, from what I have read, FBX is very versatile which is why it is popular and worth supporting.

That versatility is why even using the Autodesk FBX SDK is not goping to help get a file working in XNA.  The FBX SDK is unlikely to convert the data to match another application needs.  This means the output file may not match what XNA requires even if the file output is a valid file for some other application!

Probably the best solution would be to use the official FBX SDK for Python however that would require learning how to use that SDK as well as having to get the data right for XNA!  I'll leave that for someone else to do.

The FBX exporter that comes with Blender both for version 2.4x and version 2.5x do not produce compatible output for XNA although I assume that they do for other applications.