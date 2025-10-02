# GitHub Setup Instructions

Your local Git repository is ready! Follow these steps to push to GitHub:

## Option 1: Create Repository via GitHub Web Interface (Recommended)

### Step 1: Create the Repository on GitHub

1. Go to https://github.com/new
2. Fill in the repository details:
   - **Repository name:** `swg-mail-tracker`
   - **Description:** `Windows desktop application for syncing Star Wars Galaxies in-game mail to swgtracker.com`
   - **Visibility:** Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
3. Click **"Create repository"**

### Step 2: Push Your Local Repository

After creating the repository, GitHub will show you commands. Use these:

```bash
git remote add origin https://github.com/YOUR_USERNAME/swg-mail-tracker.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

---

## Option 2: Using GitHub CLI (If Installed)

If you have `gh` CLI installed:

```bash
# Create repository
gh repo create swg-mail-tracker --public --source=. --description="Windows desktop application for syncing Star Wars Galaxies in-game mail to swgtracker.com"

# Push to GitHub
git push -u origin main
```

For private repository, use `--private` instead of `--public`.

---

## Option 3: Manual Commands (After Creating on GitHub)

```bash
# Add GitHub remote
git remote add origin git@github.com:YOUR_USERNAME/swg-mail-tracker.git

# Push to GitHub
git push -u origin main
```

---

## Verify Your Push

After pushing, visit:
```
https://github.com/YOUR_USERNAME/swg-mail-tracker
```

You should see all your files including:
- README.md with project description
- All source code in src/
- Build scripts in build/
- Documentation files

---

## Current Repository Status

✅ Git repository initialized
✅ Initial commit created (21 files, 2647+ lines)
✅ Branch: main
✅ Ready to push

### What's Committed:

```
21 files changed, 2647 insertions(+)
├── .gitignore
├── BUILDING.md
├── PROJECT_SUMMARY.md
├── QUICK_START.md
├── README.md
├── config.example.json
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── api_client.py
│   │   ├── config_manager.py
│   │   └── file_watcher.py
│   └── gui/
│       ├── __init__.py
│       ├── main_window.py
│       ├── monitor_tab.py
│       ├── settings_tab.py
│       ├── system_tray.py
│       └── theme.py
└── utils/
    ├── __init__.py
    └── auth.py
```

---

## Recommended Repository Settings

After creating the repository on GitHub:

### About Section
- Description: `Windows desktop application for syncing Star Wars Galaxies in-game mail to swgtracker.com`
- Website: (your swgtracker.com URL if applicable)
- Topics: `python`, `swg`, `star-wars-galaxies`, `desktop-app`, `customtkinter`, `windows`

### Features to Enable
- ✅ Issues
- ✅ Discussions (optional)
- ✅ Wiki (optional)

### Branch Protection (Optional)
- Require pull request reviews
- Require status checks to pass

---

## Next Steps After Pushing

1. **Add a LICENSE file** (if you want to specify licensing)
2. **Create a GitHub Release** when you build the Windows .exe
3. **Add screenshots** to the README
4. **Set up GitHub Actions** for automated builds (optional)

---

## Troubleshooting

### "Authentication failed"
- Make sure you're logged in to GitHub
- Use a personal access token instead of password
- Or use SSH keys: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

### "Remote already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/swg-mail-tracker.git
```

### "Permission denied"
- Check your GitHub username
- Verify repository name
- Ensure you have permission to create repositories

---

## Quick Copy-Paste (After Creating Repo)

Replace `YOUR_USERNAME` with your actual GitHub username:

```bash
git remote add origin https://github.com/YOUR_USERNAME/swg-mail-tracker.git
git push -u origin main
```

That's it! Your repository will be live on GitHub.
