# GitHub Releases Guide

This guide explains how to create releases on GitHub to distribute your executable to end users.

---

## 📦 What Are GitHub Releases?

GitHub Releases allow you to:
- Distribute compiled binaries (like `.exe` files)
- Version your software
- Provide release notes and changelogs
- Let users download without needing to build from source

**Users will download from:** `https://github.com/LeeW7/swg-mail-tracker/releases`

---

## 🔨 Step 1: Build the Executable on Windows

### Prerequisites
1. Access to a Windows machine (Windows 10 or 11)
2. Python 3.10+ installed
3. Poetry installed

### Build Process

```cmd
# Clone the repository (if not already)
git clone https://github.com/LeeW7/swg-mail-tracker.git
cd swg-mail-tracker

# Run the build script
build\build.bat
```

This creates: `dist\SWGMailTracker.exe` (~25-35 MB)

### Test the Executable

**Important:** Test before releasing!

1. Copy `SWGMailTracker.exe` to a different folder
2. Double-click to run
3. Verify all features work:
   - Settings save/load
   - Directory browser
   - Test connection
   - Start/stop monitoring
   - System tray integration

---

## 🚀 Step 2: Create a GitHub Release

### Option A: Using GitHub Web Interface (Recommended)

1. **Go to your repository:**
   ```
   https://github.com/LeeW7/swg-mail-tracker
   ```

2. **Click "Releases"** (right sidebar)

3. **Click "Create a new release"** (or "Draft a new release")

4. **Choose or create a tag:**
   - Click "Choose a tag"
   - Type: `v1.0.0` (or your version number)
   - Click "Create new tag: v1.0.0 on publish"

5. **Fill in release details:**

   **Release title:**
   ```
   SWG Mail Tracker v1.0.0
   ```

   **Description:** (example)
   ```markdown
   ## 🎉 Initial Release

   First official release of SWG Mail Tracker!

   ### Features
   - ✅ Modern dark GUI matching swgtracker.com
   - ✅ Real-time file monitoring
   - ✅ System tray integration
   - ✅ Activity log with statistics
   - ✅ Easy configuration via GUI

   ### Installation
   1. Download `SWGMailTracker.exe` below
   2. Save anywhere on your computer
   3. Double-click to run
   4. Follow the [User Guide](https://github.com/LeeW7/swg-mail-tracker/blob/main/USER_GUIDE.md)

   ### Requirements
   - Windows 10 or 11
   - Active internet connection
   - SWG game installation
   - swgtracker.com account with API credentials

   ### What's New
   - Initial release

   ### Known Issues
   - None currently

   ---

   **Full Changelog:** https://github.com/LeeW7/swg-mail-tracker/commits/main
   ```

6. **Attach the executable:**
   - Drag and drop `SWGMailTracker.exe` into the "Attach binaries" area
   - Or click and browse to select it
   - Wait for upload to complete

7. **Publish:**
   - ✅ Check "Set as the latest release"
   - Click **"Publish release"**

---

### Option B: Using GitHub CLI

```bash
# From your project directory
gh release create v1.0.0 \
  dist/SWGMailTracker.exe \
  --title "SWG Mail Tracker v1.0.0" \
  --notes "Initial release - see README for details"
```

---

## 📝 Versioning Guidelines

Follow [Semantic Versioning](https://semver.org/):

- **v1.0.0** - Initial stable release
- **v1.0.1** - Bug fix (patch)
- **v1.1.0** - New feature (minor)
- **v2.0.0** - Breaking change (major)

### Version Number Format: `vMAJOR.MINOR.PATCH`

Examples:
- `v1.0.0` - First release
- `v1.0.1` - Bug fix
- `v1.1.0` - Added desktop notifications
- `v1.2.0` - Added multi-character support
- `v2.0.0` - Complete UI redesign

---

## 📋 Release Checklist

Before creating a release:

### Testing
- [ ] Build executable on clean Windows machine
- [ ] Test on Windows 10
- [ ] Test on Windows 11
- [ ] Verify all features work
- [ ] Check system tray integration
- [ ] Test with real SWG mail files
- [ ] Verify API uploads to swgtracker.com
- [ ] Check log file creation
- [ ] Test settings save/load
- [ ] Verify config.json creation

### Documentation
- [ ] Update USER_GUIDE.md if needed
- [ ] Update README.md
- [ ] Write release notes
- [ ] Update version numbers in code (if applicable)

### Repository
- [ ] All changes committed and pushed
- [ ] No pending issues blocking release
- [ ] Tag matches version number

---

## 📢 Example Release Notes Template

```markdown
## SWG Mail Tracker v1.1.0

### 🎉 What's New
- Added desktop notifications for successful uploads
- Improved error messages in activity log
- Added "Clear Statistics" button

### 🐛 Bug Fixes
- Fixed crash when mail path contains special characters
- Resolved system tray icon not appearing on some systems
- Fixed config.json not saving on first run

### 📝 Changes
- Updated CustomTkinter to v5.2.1
- Improved startup performance
- Reduced memory usage

### 📥 Installation
Download `SWGMailTracker.exe` below and follow the [User Guide](link).

### ⚠️ Known Issues
- Desktop notifications may not work on Windows Server editions

### 🔗 Links
- [User Guide](https://github.com/LeeW7/swg-mail-tracker/blob/main/USER_GUIDE.md)
- [Report Issues](https://github.com/LeeW7/swg-mail-tracker/issues)

**Full Changelog:** https://github.com/LeeW7/swg-mail-tracker/compare/v1.0.0...v1.1.0
```

---

## 🔄 Updating a Release

### To add files or change notes:

1. Go to the release page
2. Click "Edit release"
3. Make changes
4. Click "Update release"

### To delete a release:

1. Go to the release page
2. Click "Delete"
3. Confirm deletion
4. **Note:** This doesn't delete the Git tag

---

## 🏷️ Managing Tags

### Create tag manually:
```bash
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin v1.0.0
```

### Delete a tag:
```bash
# Delete locally
git tag -d v1.0.0

# Delete on GitHub
git push origin :refs/tags/v1.0.0
```

---

## 📊 After Publishing

### What users see:

1. **Releases page:**
   ```
   https://github.com/LeeW7/swg-mail-tracker/releases
   ```

2. **Latest release badge** (add to README):
   ```markdown
   ![GitHub release](https://img.shields.io/github/v/release/LeeW7/swg-mail-tracker)
   ```

3. **Download stats** - GitHub tracks download counts

### Promote your release:

- Update README.md to link to latest release
- Announce on swgtracker.com (if applicable)
- Share with SWG community
- Add to SWG forums/Discord

---

## 🔐 Release Security

### Code Signing (Optional but Recommended)

Windows SmartScreen may warn users about unsigned executables.

**To avoid warnings:**
1. Get a code signing certificate
2. Sign the .exe file
3. Users won't see SmartScreen warnings

**For now:** Users may need to click "More info" → "Run anyway"

### Checksums

Provide SHA256 checksums for verification:

```bash
# On Windows
certutil -hashfile SWGMailTracker.exe SHA256

# On macOS/Linux
shasum -a 256 SWGMailTracker.exe
```

Add to release notes:
```
### Checksums
SHA256: abc123def456...
```

---

## 🚦 Release Workflow Summary

1. **Develop** on macOS or Windows
2. **Test** thoroughly
3. **Build** on Windows (`build\build.bat`)
4. **Test** the built .exe
5. **Commit and push** all changes
6. **Create release** on GitHub
7. **Upload** SWGMailTracker.exe
8. **Publish** release
9. **Announce** to users

---

## 💡 Pro Tips

### Pre-release versions

For beta testing:
- Tag as `v1.0.0-beta.1`
- Check "This is a pre-release"
- Users see it's not production-ready

### Automated builds (Advanced)

Use GitHub Actions to build automatically:
- Create `.github/workflows/build.yml`
- Build on every tag push
- Automatically attach .exe to release

### Multiple files

You can attach:
- `SWGMailTracker.exe` (required)
- `USER_GUIDE.pdf` (optional)
- `config.example.json` (optional)
- Source code (GitHub adds automatically)

### Draft releases

Create draft releases to prepare before publishing:
- Write release notes in advance
- Upload files
- Publish when ready

---

## 📞 Getting Help

- **GitHub Docs:** https://docs.github.com/en/repositories/releasing-projects-on-github
- **This repository:** https://github.com/LeeW7/swg-mail-tracker

---

**Ready to release?** Follow Step 1 (build) and Step 2 (create release), and your users can start downloading! 🎉
