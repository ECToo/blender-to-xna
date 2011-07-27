REM Copy newer files to the U drive
REM Excludes all OBJ and BIN folders
robocopy.exe . "U:\My Documents\Home\My Stuff\XNA\BlenderToXNA" /MIR /XO /XD obj bin .svn *.user *.suo *.cachefile
