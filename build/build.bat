@echo off
REM Build script for SWG Mail Tracker on Windows

echo ========================================
echo SWG Mail Tracker - Build Script
echo ========================================
echo.

REM Check if Poetry is installed
where poetry >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Poetry is not installed or not in PATH
    echo Please install Poetry first: https://python-poetry.org/docs/#installation
    pause
    exit /b 1
)

echo [1/4] Installing dependencies...
poetry install
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [2/4] Cleaning previous builds...
if exist dist rmdir /s /q dist
if exist build\output rmdir /s /q build\output

echo.
echo [3/4] Building executable with PyInstaller...
poetry run pyinstaller build\build.spec --clean --distpath dist --workpath build\output
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Build failed
    pause
    exit /b 1
)

echo.
echo [4/4] Build complete!
echo.
echo Executable location: dist\SWGMailTracker.exe
echo.
echo ========================================
echo Build completed successfully!
echo ========================================
pause
