echo off
python -i newlook.py
color
cls
if %errorlevel% not 0 exit
else echo %errorlevel%