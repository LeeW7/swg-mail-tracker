# SWG Mail Tracker - User Guide

**Automatically sync your Star Wars Galaxies in-game mail to swgtracker.com**

---

## 📥 Installation

### Download the Application

1. Go to the [**Releases page**](https://github.com/LeeW7/swg-mail-tracker/releases)
2. Download the latest **`SWGMailTracker.exe`**
3. Save it anywhere on your computer (Desktop, Documents, etc.)

**That's it!** No installation required. No Python. No dependencies.

### ⚠️ Windows Defender / SmartScreen Warning

**This is completely normal and expected!** Since this application is not digitally signed with a paid certificate, Windows will show security warnings.

#### When Downloading (Browser Warning)

**Microsoft Edge / Chrome:**
1. Your browser may block the download with a warning
2. Click on the **three dots (...)** or **"Show more"**
3. Click **"Keep"** or **"Keep anyway"**

**Why this happens:** Unsigned .exe files trigger browser protection. This is a false positive - the app is safe.

#### When Running (Windows Defender SmartScreen)

**First-time launch warning:**

When you double-click `SWGMailTracker.exe`, Windows may show:

```
Windows protected your PC
Microsoft Defender SmartScreen prevented an unrecognized app from starting.
```

**To run the application:**

1. Click **"More info"** (small blue text)
2. Click **"Run anyway"** button
3. The app will start normally

**Alternative method - Unblock the file:**

1. Right-click on `SWGMailTracker.exe`
2. Select **Properties**
3. At the bottom, check the box: **☑️ Unblock**
4. Click **Apply** → **OK**
5. Now double-click to run normally

#### Windows Defender Antivirus Alert

If Windows Defender flags the file:

1. Open **Windows Security** (search in Start menu)
2. Go to **Virus & threat protection**
3. Click **Protection history**
4. Find the `SWGMailTracker.exe` alert
5. Click **Actions** → **Allow**

**Or add an exclusion:**

1. Open **Windows Security**
2. Go to **Virus & threat protection**
3. Click **Manage settings** (under "Virus & threat protection settings")
4. Scroll down to **Exclusions**
5. Click **Add or remove exclusions**
6. Click **Add an exclusion** → **File**
7. Browse to and select `SWGMailTracker.exe`

#### Why Does This Happen?

This application is built with PyInstaller, which packages Python applications into executables. Windows flags unsigned executables from unknown publishers as a security precaution.

**This is a false positive.** The application:
- ✅ Is open source (you can view all code on GitHub)
- ✅ Only connects to swgtracker.com
- ✅ Only reads your SWG mail files
- ✅ Stores settings locally in config.json
- ✅ Does not collect or send any personal data

**Why not sign it?** Code signing certificates cost $100-400/year from trusted authorities. This is a free, community tool.

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

#### 2. SWG Mail Directories (Multiple Characters)

You can add up to **4 character mail folders**:

- Enter an optional character name (e.g., "Main Tank", "Trader") to help identify each folder
- Browse to each character's mail folder
- Click **"+ Add Character"** to add more folders (up to 4 total)
- Use the **×** button to remove a folder

**Example:** If you have multiple characters, the app will monitor all their mail folders simultaneously!

#### 3. API Key

You need to get your API Key from swgtracker.com:

**To find your API Key:**
1. Log in to swgtracker.com
2. Go to your account settings or API section
3. Copy your **API Key** (also called Scanner User Key)
4. Paste it into the application

**Note:** You only need the API Key - no User ID required!

#### 4. Application Preferences (Optional)

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

The app now supports **up to 4 characters simultaneously**!

1. Go to **Settings** tab
2. Click **"+ Add Character"** to add more mail folders
3. Enter an optional label for each character (e.g., "Main", "Alt", "Trader")
4. Browse to each character's mail folder
5. Click **Save Settings**
6. Start monitoring - all folders will be watched at once!

**No need to stop/start or run multiple instances!** The app monitors all configured folders simultaneously.

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
