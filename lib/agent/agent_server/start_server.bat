@echo off

set x=%~d0
set y=%~dp0
%x%
cd %y%
python agent_server.py
pause
