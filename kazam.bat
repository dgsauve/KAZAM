@echo off
set "PREV_DIR=%CD%"
cd /d "%~dp0"
python src\main.py %*
cd /d "%PREV_DIR%"