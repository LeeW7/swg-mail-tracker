# SWG Mail Tracker

**Windows desktop application for syncing Star Wars Galaxies in-game mail files to swgtracker.com**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

---

## 📥 For End Users

**Looking to use the app?** See the **[User Guide](USER_GUIDE.md)** for simple download and installation instructions.

**Download:** Go to [Releases](https://github.com/LeeW7/swg-mail-tracker/releases) and download the latest `SWGMailTracker.exe`

---

## 🎨 Features

- ✅ **Modern dark GUI** matching swgtracker.com aesthetic
- ✅ **Real-time file monitoring** with watchdog
- ✅ **System tray integration** - runs in the background
- ✅ **Activity log** with color-coded messages
- ✅ **Statistics tracking** - processed, uploaded, errors
- ✅ **Easy configuration** - visual settings interface
- ✅ **Standalone executable** - no dependencies required for end users
- ✅ **Cross-platform development** - develop on macOS, build on Windows

---

## 🛠️ For Developers

### Prerequisites

- **Python 3.10+**
- **Poetry** (dependency management)
- **Git**

### Development Setup

```bash
# Clone the repository
git clone https://github.com/LeeW7/swg-mail-tracker.git
cd swg-mail-tracker

# Install dependencies
poetry install

# Run the application
poetry run python src/main.py
```

### Technology Stack

- **GUI:** CustomTkinter 5.2.0
- **File Monitoring:** watchdog 3.0.0
- **HTTP Requests:** requests 2.31.0
- **System Tray:** pystray 0.19.5
- **Build Tool:** PyInstaller 6.0.0

### Project Structure

```
swg-mail-tracker/
├── src/
│   ├── main.py                 # Application entry point
│   ├── gui/
│   │   ├── main_window.py      # Main application window
│   │   ├── settings_tab.py     # Settings configuration
│   │   ├── monitor_tab.py      # Monitoring & activity log
│   │   ├── system_tray.py      # System tray integration
│   │   └── theme.py            # Color palette & fonts
│   ├── core/
│   │   ├── config_manager.py   # JSON configuration
│   │   ├── file_watcher.py     # Watchdog implementation
│   │   └── api_client.py       # swgtracker.com API
│   └── resources/              # Icons and assets
├── utils/
│   └── auth.py                 # Legacy auth module
├── build/
│   ├── build.spec              # PyInstaller configuration
│   ├── build.bat               # Windows build script
│   └── build.sh                # macOS build script
├── pyproject.toml              # Poetry dependencies
└── config.example.json         # Configuration template
```

---

## 🔨 Building

### Build on Windows

```cmd
# Run the build script
build\build.bat

# Or manually
poetry install
poetry run pyinstaller build\build.spec --clean
```

The executable will be created in `dist\SWGMailTracker.exe` (~25-35 MB).

### Build on macOS (for testing)

```bash
chmod +x build/build.sh
./build/build.sh
```

**Note:** Final distribution should be built on Windows for Windows users.

See **[BUILDING.md](BUILDING.md)** for detailed build instructions.

---

## 📚 Documentation

- **[USER_GUIDE.md](USER_GUIDE.md)** - End user instructions (download, setup, usage)
- **[QUICK_START.md](QUICK_START.md)** - Quick start for developers
- **[BUILDING.md](BUILDING.md)** - Detailed build instructions
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Complete project overview

---

## 🚀 Creating a Release

See **[RELEASE_GUIDE.md](RELEASE_GUIDE.md)** for instructions on creating GitHub Releases.

Quick version:
1. Build the .exe on Windows
2. Create a new release on GitHub
3. Upload the .exe file
4. Users download from the Releases page

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

### Development Workflow

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📝 Configuration

The application creates a `config.json` file on first run:

```json
{
    "mail_path": "C:\\SWG Restoration III\\profiles\\character\\mail_CharacterName",
    "scanner_user_id": "",
    "scanner_user_key": "",
    "start_with_windows": false,
    "minimize_to_tray": true,
    "show_notifications": true,
    "auto_start_monitoring": false
}
```

All settings can be configured through the GUI - no manual editing required.

---

## 🐛 Troubleshooting

Check the application log file: `swg_mail_tracker.log`

Common issues and solutions are in the [User Guide](USER_GUIDE.md#-troubleshooting).

---

## 📊 Design Philosophy

- **User-friendly:** Simple GUI that matches swgtracker.com
- **Lightweight:** Minimal resource usage
- **Reliable:** Comprehensive error handling
- **Transparent:** Clear activity logging
- **Standalone:** No external dependencies for end users

---

## 🎯 Roadmap

- [ ] Windows desktop notifications
- [ ] Custom application icon
- [ ] "Start with Windows" registry integration
- [ ] Auto-update functionality
- [ ] Multi-character profile support
- [ ] Offline queue for failed uploads

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 🙏 Acknowledgments

- Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Inspired by the original SWGTrackerMailImport.py script
- Design matches [swgtracker.com](https://swgtracker.com)

---

## 📧 Support

- **Issues:** [GitHub Issues](https://github.com/LeeW7/swg-mail-tracker/issues)
- **Discussions:** [GitHub Discussions](https://github.com/LeeW7/swg-mail-tracker/discussions)

---

**Happy tracking!** 🚀
