REM Copy the install files to another folder ready to zip up
REM Excludes all Visual Studio OBJ BIN and Subversion folders
robocopy.exe .\current ..\BlenderToXNA /MIR /XO /XD obj bin .svn *.user *.suo *.cachefile
copy ReadMe.htm ..\BlenderToXNA
