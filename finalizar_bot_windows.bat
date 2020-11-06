@echo off
@echo finalizando bot ...
echo %time%
taskkill /IM "python.exe" /F
timeout 5 > NUL
echo %time%