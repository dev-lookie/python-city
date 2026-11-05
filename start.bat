@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (set PYTHON=py) else (set PYTHON=python)
start "python city" cmd /k %PYTHON% main.py
