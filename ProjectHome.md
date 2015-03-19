## Introduction ##
This project is used for work in progress test versions.  The final version is included with the Blender distribution.  Please use the version that ships with Blender.

The 'unified' folder in this project is work in progress to create one script to ship with Blender that works with most applications including XNA.

The Blender wiki page will be updated with progress:
http://wiki.blender.org/index.php/Extensions:2.5/Py/Scripts/Import-Export/UnifiedFBX


## Purpose ##
XNA 4.0 uses features of the FBX file format that are not included in the original FBX exporter that ships with Blender.  These scripts are to ensure that an FBX export is available that works with XNA.

UDK, Unity, XNA and Sunburn all require the FBX output in slightly different ways to look best or even to load at all in those environments.  Where possible the scripts are being unified with options so that a single export script will suit as many applications as possible.


## Instructions ##
Just enable the addon in User Preferences.

For instructions on how these scripts were intended to be used and some tips for creating models that work with XNA, see my blog:


http://blog.diabolicalgame.co.uk/2011/07/exporting-animated-models-from-blender.html

or the Blender Wiki:

http://wiki.blender.org/index.php/Extensions:2.5/Py/Scripts/Import-Export/Blender-toXNA



### Dependencies ###
**XNA** is the development framework Microsoft has created for independent and hobby developers to use for games. It is based on Microsoft .Net and C#.

http://create.msdn.com/

**Blender** is a fully featured 3D modelling application.  Open Source, completely free and actively supported and developed by a strong community.

http://www.blender.org/