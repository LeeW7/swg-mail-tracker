# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for SWG Mail Tracker
"""
import os
from pathlib import Path

block_cipher = None

# Get absolute paths
spec_root = Path(SPECPATH).parent
icon_path = spec_root / 'src' / 'resources' / 'icon.ico'

a = Analysis(
    ['../src/main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('../src/resources/*', 'resources'),
    ],
    hiddenimports=[
        'PIL._tkinter_finder',
        'customtkinter',
        'watchdog',
        'pystray',
        'requests',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SWGMailTracker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window for GUI app
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(icon_path) if icon_path.exists() else None,
    version_file=None,
)
