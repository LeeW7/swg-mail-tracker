# Building SWG Mail Tracker

## Prerequisites

### Windows (Recommended for final build)
- Python 3.10 or higher
- Poetry (Python package manager)
- Git (optional)

### macOS (Development only)
- Python 3.10 or higher
- Poetry

---

## Installation Steps

### 1. Install Python

Download and install Python 3.10+ from:
- Windows: https://www.python.org/downloads/windows/
- macOS: `brew install python@3.10`

Verify installation:
```bash
python --version
# Should show Python 3.10 or higher
```

### 2. Install Poetry

**Windows (PowerShell):**
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

**macOS/Linux:**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Add Poetry to PATH as instructed by the installer.

Verify installation:
```bash
poetry --version
```

### 3. Clone or Download Project

```bash
cd /path/to/your/projects
git clone <repository-url>
cd swg-mail-tracker
```

Or download and extract the ZIP file.

---

## Development Setup

### Install Dependencies

```bash
poetry install
```

This will:
- Create a virtual environment
- Install all required packages
- Set up development dependencies

### Run in Development Mode

```bash
poetry run python src/main.py
```

---

## Building the Executable

### Windows Build (Primary Target)

1. Open Command Prompt or PowerShell in the project directory

2. Run the build script:
   ```cmd
   build\build.bat
   ```

   Or manually:
   ```cmd
   poetry install
   poetry run pyinstaller build\build.spec --clean
   ```

3. The executable will be created in:
   ```
   dist\SWGMailTracker.exe
   ```

### macOS Build (Development Testing Only)

```bash
chmod +x build/build.sh
./build/build.sh
```

**Note:** The macOS build is for development testing only. The final application should be built on Windows for Windows users.

---

## Build Output

### What Gets Created

```
dist/
└── SWGMailTracker.exe    # Standalone executable (~25-35 MB)
```

### Distribution

The `SWGMailTracker.exe` file is completely standalone:
- No Python installation required
- No dependencies needed
- Can be run from any location
- Creates `config.json` on first run

### File Size

Expected size: **25-35 MB**
- Includes Python runtime
- Includes all libraries (CustomTkinter, watchdog, etc.)
- Compressed with UPX

---

## Build Configuration

### Customizing the Build

Edit `build/build.spec` to customize:

- **Application name:** Change `name='SWGMailTracker'`
- **Icon:** Set `icon='path/to/icon.ico'`
- **Console window:** `console=False` (no console) or `console=True` (show console)
- **Compression:** `upx=True` (compress) or `upx=False` (no compression)

### Adding an Icon

1. Create or download a `.ico` file (256x256 recommended)
2. Save it as `src/resources/icon.ico`
3. Rebuild the application

---

## Troubleshooting Build Issues

### "Poetry not found"
- Ensure Poetry is installed and in PATH
- Restart terminal/command prompt
- Try: `python -m poetry` instead of `poetry`

### "Module not found" errors during build
- Run `poetry install` to ensure all dependencies are installed
- Check `pyproject.toml` for missing dependencies
- Add missing modules to `hiddenimports` in `build.spec`

### Build succeeds but .exe crashes
- Check `swg_mail_tracker.log` for errors
- Try running with console enabled: `console=True` in build.spec
- Verify all resources are included in `datas` section

### Large executable size
- Ensure UPX is enabled: `upx=True`
- Remove unused imports from code
- Consider using `--onedir` instead of `--onefile`

### "Permission denied" errors
- Run Command Prompt/PowerShell as Administrator
- Disable antivirus temporarily during build
- Check file permissions

---

## Cross-Platform Development Workflow

### Develop on macOS, Build on Windows

1. **Develop on macOS:**
   ```bash
   poetry run python src/main.py
   ```

2. **Test changes:**
   - Run the application
   - Test all features
   - Commit changes to Git

3. **Build on Windows:**
   - Pull latest changes
   - Run `build\build.bat`
   - Test the executable

This is the recommended workflow for this project.

---

## Creating an Installer (Optional)

### Using Inno Setup (Windows)

1. Download Inno Setup: https://jrsoftware.org/isdl.php

2. Create `installer.iss` script:
   ```iss
   [Setup]
   AppName=SWG Mail Tracker
   AppVersion=1.0.0
   DefaultDirName={pf}\SWGMailTracker
   OutputBaseFilename=SWGMailTracker-Setup

   [Files]
   Source: "dist\SWGMailTracker.exe"; DestDir: "{app}"

   [Icons]
   Name: "{commonprograms}\SWG Mail Tracker"; Filename: "{app}\SWGMailTracker.exe"
   ```

3. Compile with Inno Setup Compiler

---

## Distribution Checklist

Before releasing:

- ✅ Test on clean Windows machine
- ✅ Verify no external dependencies required
- ✅ Test all features (monitoring, settings, system tray)
- ✅ Check log file creation and permissions
- ✅ Verify config.json is created on first run
- ✅ Test with real SWG mail files
- ✅ Include README.md and QUICK_START.md
- ✅ Create release notes

---

## Next Steps After Building

1. Copy `SWGMailTracker.exe` to desired location
2. Run the executable
3. Configure settings (mail path, API credentials)
4. Start monitoring!

---

## Development Dependencies

Installed automatically by Poetry:

### Runtime
- `customtkinter` - Modern GUI framework
- `watchdog` - File system monitoring
- `requests` - HTTP requests
- `pystray` - System tray integration
- `pillow` - Image handling

### Development
- `pyinstaller` - Executable builder
- `pytest` - Testing framework

---

## Support

For build issues:
1. Check this guide thoroughly
2. Review `swg_mail_tracker.log`
3. Check PyInstaller output for errors
4. Ensure all prerequisites are installed
