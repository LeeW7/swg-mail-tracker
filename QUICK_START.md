# Quick Start Guide

## Development (macOS)

### 1. Install Dependencies

```bash
cd swg-mail-tracker
poetry install
```

### 2. Run the Application

```bash
poetry run python src/main.py
```

### 3. Configure Settings

1. Click on the **Settings** tab
2. Browse to your SWG mail directory (e.g., `C:\SWG Restoration III\profiles\character\Restoration\mail_CharacterName`)
3. Enter your **Scanner User ID** from swgtracker.com
4. Enter your **Scanner User Key** (API Key) from swgtracker.com
5. Click **Save Settings**

### 4. Test Connection

Click the **Test Connection** button to verify your API credentials.

### 5. Start Monitoring

Click **Start Monitoring** to begin watching for new mail files.

---

## Building for Windows

### On Windows Machine:

1. Install Python 3.10+ and Poetry
2. Clone the repository
3. Run the build script:

```cmd
build\build.bat
```

The executable will be created in `dist\SWGMailTracker.exe`

### Alternative Manual Build:

```cmd
poetry install
poetry run pyinstaller build\build.spec --clean
```

---

## Features

- ✅ **Dark Theme** matching swgtracker.com
- ✅ **Real-time Monitoring** of SWG mail directory
- ✅ **System Tray** integration
- ✅ **Activity Log** with color-coded messages
- ✅ **Statistics Tracking** (files processed, uploaded, errors)
- ✅ **Auto-start** monitoring option
- ✅ **Desktop Notifications** for uploads

---

## Troubleshooting

### "Mail path does not exist"
Make sure the path points to your SWG mail directory. On Windows, it typically looks like:
```
C:\SWG Restoration III\profiles\YourCharacter\Restoration\mail_YourCharacterName
```

### "Connection test failed"
- Check your internet connection
- Verify User ID and API Key are correct
- Check if swgtracker.com is accessible

### Application won't start
- Check `swg_mail_tracker.log` for errors
- Ensure Python 3.10+ is installed
- Try reinstalling dependencies: `poetry install`

---

## Configuration File

Settings are stored in `config.json`:

```json
{
    "mail_path": "path/to/swg/mail",
    "scanner_user_id": "your_id",
    "scanner_user_key": "your_key",
    "start_with_windows": false,
    "minimize_to_tray": true,
    "show_notifications": true,
    "auto_start_monitoring": false
}
```

You can manually edit this file if needed.

---

## Getting API Credentials

1. Visit https://swgtracker.com
2. Log in to your account
3. Navigate to Settings or API section
4. Find your **Scanner User ID** and **Scanner User Key**
5. Copy them into the Settings tab of the application

---

## Support

For issues or questions:
- Check the log file: `swg_mail_tracker.log`
- Review this guide
- Check your configuration

---

Happy tracking! 🚀
