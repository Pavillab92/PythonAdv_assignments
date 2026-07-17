@echo off

:: SET CUSTOM SCRIPTS
set "SCRIPT_PATH=D:\Documentos\My Maya Projects\customBootup"
set "IMG_PATH=%SCRIPT_PATH%\icons"
set "PYTHONPATH=%SCRIPT_PATH%;%PYTHONPATH%"
set "XBMLANGPATH=%IMG_PATH%;%XBMLANGPATH%"


:: START MAYA
set "MAYA_VERSION=2023"
set "MAYA_PATH=C:\Program Files\Autodesk\Maya%MAYA_VERSION%\bin\"
start "" "%MAYA_PATH%maya.exe"

exit