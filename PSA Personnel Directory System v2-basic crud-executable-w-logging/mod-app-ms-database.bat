@ECHO OFF
SET filedir=%~dp0
ECHO ============================
ECHO Running files in:
ECHO %filedir%
ECHO DO NOT CLOSE SERVER WINDOW!
ECHO ============================
CD %filedir%/DB Browser for SQLite Portable v.3.1.2
START SQLiteDatabaseBrowserPortable.exe