#!/bin/bash
# Build script for SWG Mail Tracker (macOS/Linux - for development testing only)

set -e

echo "========================================"
echo "SWG Mail Tracker - Build Script"
echo "========================================"
echo

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "ERROR: Poetry is not installed"
    echo "Please install Poetry first: https://python-poetry.org/docs/#installation"
    exit 1
fi

echo "[1/4] Installing dependencies..."
poetry install

echo
echo "[2/4] Cleaning previous builds..."
rm -rf dist
rm -rf build/output

echo
echo "[3/4] Building executable with PyInstaller..."
poetry run pyinstaller build/build.spec --clean --distpath dist --workpath build/output

echo
echo "[4/4] Build complete!"
echo
echo "Executable location: dist/SWGMailTracker"
echo
echo "========================================"
echo "Build completed successfully!"
echo "========================================"
