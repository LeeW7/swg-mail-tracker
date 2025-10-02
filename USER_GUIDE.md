# SWG Mail Tracker - User Guide

**Automatically sync your Star Wars Galaxies in-game mail to swgtracker.com**

---

## 📥 Installation

### Download the Application

1. Go to the [**Releases page**](https://github.com/LeeW7/swg-mail-tracker/releases)
2. Download the latest **`SWGMailTracker.exe`**
3. Save it anywhere on your computer (Desktop, Documents, etc.)

**That's it!** No installation required. No Python. No dependencies.

---

## 🚀 First Time Setup

### Step 1: Launch the Application

Double-click **`SWGMailTracker.exe`** to start the application.

The app will open with a dark-themed interface matching swgtracker.com.

### Step 2: Configure Your Settings

Click on the **Settings** tab and enter the following:

#### 1. SWG Mail Directory

Click the **Browse** button and navigate to your SWG mail folder.

**Example path:**
```
C:\SWG Restoration III\profiles\YourCharacter\Restoration\mail_YourCharacterName
```

**How to find it:**
- Open your SWG game folder
- Navigate to `profiles\[YourCharacter]\Restoration\`
- Look for a folder starting with `mail_`

#### 2. API Credentials

You need to get these from swgtracker.com:

**Scanner User ID:**
- Log in to swgtracker.com
- Go to your account settings or API section
- Copy your Scanner User ID

**Scanner User Key (API Key):**
- In the same location on swgtracker.com
- Copy your Scanner User Key or API Key

Paste both into the application.

#### 3. Application Preferences (Optional)

- ☑️ **Minimize to system tray** - App hides in system tray when minimized
- ☑️ **Show desktop notifications** - Get notified when mail is uploaded
- ☐ **Auto-start monitoring** - Automatically start watching when app launches

### Step 3: Save Your Settings

Click the **Save Settings** button at the bottom.

You'll see a success message in the Monitor tab.

---

## ▶️ Using the Application

### Starting Monitoring

1. Go to the **Monitor** tab
2. Click the **Start Monitoring** button in the top-right

The status will change to:
- **● Monitoring Active** (green indicator)
- You'll see the message "Monitoring started" in the activity log

### What Happens Now?

The application is now watching your SWG mail folder. When you receive new in-game mail:

1. ✅ Mail file is automatically detected
2. ✅ Content is read and uploaded to swgtracker.com
3. ✅ You'll see a success message in the Activity Log
4. ✅ Statistics update (Files Processed, Successfully Uploaded)

### Stopping Monitoring

Click the **Stop Monitoring** button when you're done playing.

### Testing Your Connection

Before starting monitoring, you can verify your API credentials:

1. Click the **Test Connection** button
2. Watch the Activity Log for:
   - ✅ **"Connection successful"** (green) - You're all set!
   - ❌ **"Connection failed"** (red) - Check your credentials

---

## 📊 Understanding the Monitor Tab

### Status Section
- **Indicator:** Green dot = monitoring active, Gray dot = not monitoring
- **Status Text:** Shows current monitoring state

### Statistics
- **Files Processed:** Total mail files detected
- **Successfully Uploaded:** Files uploaded to swgtracker.com
- **Errors:** Failed uploads (check Activity Log for details)

### Activity Log
Color-coded messages show what's happening:
- 🔵 **Blue (Info):** General information
- 🟢 **Green (Success):** Successful uploads
- 🔴 **Red (Error):** Failed uploads or errors
- 🟡 **Yellow (Warning):** Warnings (like empty files)

You can clear the log anytime with the **Clear Log** button.

---

## 🎛️ System Tray

When you minimize the application (if "Minimize to system tray" is enabled):

- Look for the **green icon** in your Windows system tray
- **Right-click** the icon for options:
  - **Show** - Bring window back
  - **Start Monitoring** - Start watching for mail
  - **Stop Monitoring** - Stop watching
  - **Exit** - Close the application

**Tip:** The app keeps running in the background, so you can minimize it while playing SWG!

---

## ❓ Troubleshooting

### "Mail path does not exist"

**Solution:**
- Double-check your SWG installation path
- Make sure you're pointing to the `mail_CharacterName` folder, not just `mail`
- The folder must exist (created after receiving at least one in-game mail)

### "Connection test failed"

**Solutions:**
- Verify you're connected to the internet
- Check that swgtracker.com is accessible
- Confirm your User ID and API Key are correct (no extra spaces)
- Make sure your swgtracker.com account is active

### "Files detected but not uploading"

**Solutions:**
- Check the Activity Log for specific error messages
- Verify your API credentials are still valid
- Make sure the mail files aren't empty
- Check `swg_mail_tracker.log` for detailed errors

### Application won't start

**Solutions:**
- Make sure you downloaded the correct file (`SWGMailTracker.exe`)
- Check Windows Defender or antivirus isn't blocking it
- Try running as Administrator (right-click → Run as administrator)
- Redownload the file (it might be corrupted)

### "How do I uninstall?"

Simply delete the `SWGMailTracker.exe` file and the `config.json` file (created in the same folder).

---

## 📁 Configuration File

The app creates a `config.json` file in the same folder as the .exe.

**This file stores your settings:**
- Mail directory path
- API credentials
- Preferences

**Backup tip:** Save a copy of `config.json` to quickly restore your settings on another computer.

---

## 🔒 Privacy & Security

- Your API credentials are stored locally in `config.json`
- Mail content is sent directly to swgtracker.com (HTTPS)
- No data is collected or sent anywhere else
- The application runs entirely on your computer

---

## 💡 Tips & Best Practices

### Recommended Workflow

1. **Start SWG Mail Tracker before launching the game**
2. **Click "Start Monitoring"**
3. **Minimize to system tray** (keeps it out of the way)
4. **Play SWG normally** - mail is synced automatically
5. **Stop monitoring when done** (or leave it running!)

### Multiple Characters

If you play multiple characters:

1. Stop monitoring
2. Go to Settings
3. Browse to the different character's mail folder
4. Save settings
5. Start monitoring again

**Or:** Run multiple instances of the app (one per character), just copy the .exe to different folders.

### Always Running

Want mail to sync 24/7?

1. Enable **"Auto-start monitoring"** in Settings
2. Create a Windows shortcut to the .exe
3. Place shortcut in `shell:startup` folder (press Win+R, type `shell:startup`)
4. App will launch automatically when Windows starts

---

## 🆘 Getting Help

### Check the Logs

The app creates a log file: `swg_mail_tracker.log`

This file contains detailed information about errors and activity.

### Common Questions

**Q: Do I need to keep the app running?**
A: Only when you want mail to be synced. You can start/stop it anytime.

**Q: Does it use a lot of resources?**
A: No! It uses minimal CPU/memory while monitoring.

**Q: Can I move the .exe file?**
A: Yes! Just move it anywhere and run it. Your settings will reset, but you can reconfigure.

**Q: Does it work with SWG Legends, Restoration, etc.?**
A: Yes! Works with any SWG server as long as swgtracker.com supports it.

**Q: What happens if I'm offline?**
A: Mail files will be detected, but uploads will fail. Just restart monitoring when back online.

---

## 📝 Version History

Check the [Releases page](https://github.com/LeeW7/swg-mail-tracker/releases) for:
- Latest version
- Changelog
- Bug fixes
- New features

---

## 🎮 Happy Tracking!

Now you can focus on playing SWG while your mail automatically syncs to swgtracker.com!

**Questions or issues?** Check the GitHub repository: https://github.com/LeeW7/swg-mail-tracker
