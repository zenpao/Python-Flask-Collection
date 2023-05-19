@ECHO OFF
SET filedir=%~dp0
ECHO ============================
ECHO Running files in:
ECHO %filedir%
ECHO DO NOT CLOSE SERVER WINDOW!
ECHO ============================
CD %filedir%
START cmd.exe /k app.py
START http://127.0.0.1:5000/