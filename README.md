# SWG Mail Tracker

Desktop application for syncing Star Wars Galaxies in-game mail files to swgtracker.com.

## Features

- Modern GUI with dark theme matching swgtracker.com
- Real-time file monitoring for SWG mail files
- System tray integration
- Easy configuration management
- Cross-platform development (develop on macOS, package on Windows)

## Development Setup

### Prerequisites
- Python 3.10+
- Poetry

### Installation

```bash
# Install dependencies
poetry install

# Run the application
poetry run python src/main.py
```

## Building for Windows

On Windows machine:

```bash
# Build executable
poetry run pyinstaller build/build.spec --clean
```

Output will be in `dist/` directory.

## Configuration

Configuration is stored in `config.json`:

```json
{
    "mail_path": "C:\\SWG Restoration III\\profiles\\...",
    "scanner_user_id": "your_user_id",
    "scanner_user_key": "your_api_key",
    "start_with_windows": false,
    "minimize_to_tray": true,
    "show_notifications": true
}
```

## Project Structure

```
swg-mail-tracker/
├── src/
│   ├── main.py                 # Application entry point
│   ├── gui/                    # GUI components
│   ├── core/                   # Core functionality
│   └── resources/              # Icons and assets
├── utils/                      # Utility modules
├── build/                      # Build configuration
└── pyproject.toml             # Dependencies
```

## License

MIT
