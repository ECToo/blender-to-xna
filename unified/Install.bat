@echo This script must be run as an administrator
@echo (Right click 'Run as administrator')
@echo ================================================================
@echo IO_SCENE_FBX
@echo ================================================================
@echo Deletes the contents of the above Blender script folder and the
@echo associated cache files and replaces with the new scripts.
@echo ================================================================
@pause
@cd /d %~dp0
@del "C:\Program Files\Blender Foundation\Blender\2.58\scripts\addons\io_scene_fbx\*.*" /S /Q
@copy ".\io_scene_fbx\*.*" "C:\Program Files\Blender Foundation\Blender\2.58\scripts\addons\io_scene_fbx"
@pause
