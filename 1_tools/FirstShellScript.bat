:: MY FIRST SHELL SCRIPT

echo "This is a print"

:: CREATE VARIABLES
set firstVariable = "This is how you create a variable."
:: CALL VARIABLES
echo %firstVariable%

:: DOSKEY CREATES ALIASES FOR COMMANDS, LET'S OPEN EDGE
doskey openEdge="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" $*
openEdge

:: EXTRA INFORMATION ON COMMANDS, USE HELP + COMMAND
help dir

::CHANGE DIRECTORY
:: If directory is in a different partition first change partition before changing directory.
D:
cd "D:\Documentos\AR Python Workshop\Python Advanced\Week 1 - Tools\assignment"

::*********************************************************************
:: CAUTION FILE TAMPERING
::*********************************************************************

:: CREATE NEW DIRECTORY
md "shell_test"

:: CREATE AN EMPTY FILE
type nul > filename.txt

:: CREATE A FILE WITH SOME CODE INNIT
echo print('File created with Shell Command') > test_print.py

:: RENAME A FILE: ren old name new name
ren test_print.py new_test_print.py

:: TAKE A LOOK AT WHAT IS INSIDE DIRECTORIES
dir shell_test

:: TAKE A LOOK AT THE DIRECTORY'S PERMITS
icacls shell_test

:: EXECUTE A PYTHON FILE WITH SHELL: python filename.py
python new_test_print.py

:: CAUTION DELETE ITEMS (deletes files only not folders)
:: del shell_test