@echo off
echo Adding TOI-ZERO to PATH...
echo.

:: Add current directory to user PATH
setx PATH "%PATH%;%~dp0"

echo.
echo Setup complete! You can now use 'toi' from any directory.
echo.
echo Example commands:
echo   toi pull A1-001
echo   toi run A1-001.py
echo   toi submit A1-001.py
echo   toi status A1-001
echo.
echo Please restart your terminal for changes to take effect.
