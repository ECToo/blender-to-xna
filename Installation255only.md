# Introduction #

These scripts are shipped with the download for version 2.56 onwards.  There is no need to install anything.

The scripts on this site only need to be installed if you are still using version 2.55 Beta of Blender.  It is recommended that you upgrade to Blender 2.56 or above.

# Old Instructions #

The scripts are provided as a package and they should be installed in the appropriate folder.  Be careful if you rename anything because class and folder names may be included in the scripts.

# Location #

The scripts are included in one package which should be installed in a sub folder of the 'addons' folder.

Depending on the settings used while installing Blender the scripts may be in different locations.  On Windows if you accepted the default the scripts should be in the users application data folder:

"C:\Users\%USERNAME%\AppData\Roaming\Blender Foundation\Blender\2.5x\scripts\addons"

or on a network:

"%USERPROFILE%\AppData\Roaming\Blender Foundation\Blender\2.5x\scripts\addons"

The AppData folder is usually hidden.

# Installation #

Make sure you have exited Blender.
If you are re-installing you must delete the compiled Python files from the install folder otherwise Blender will use the old scripts.  The compiled files are the ones ending .pyc.
You can just delete all the files in the package folder as you are about to replace them anyway.

Copy all the script files in to the install folder.  Typically that is one "init.py" file and one or more class files, such as 'export.py'.

Start Blender and bring up the File->User Preferences menu.  Select the 'Addons' tab, find the new script from the list and enable it by puting a tick (check) in the small box.  If you want that to start every time you start Blender you will need to press 'Save Default'.  If you have a model file open that also gets saved as part of the default!

If the script is an export script it will then be available on the File->Export menu.