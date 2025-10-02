"""
Settings tab for configuration management
"""
import customtkinter as ctk
from tkinter import filedialog
import logging
from typing import Callable
from .theme import COLORS, FONTS

logger = logging.getLogger(__name__)


class SettingsTab(ctk.CTkFrame):
    """Settings configuration tab"""

    def __init__(self, master, config_manager, on_save_callback: Callable = None):
        """
        Initialize settings tab

        Args:
            master: Parent widget
            config_manager: ConfigManager instance
            on_save_callback: Optional callback when settings are saved
        """
        super().__init__(master)
        self.config_manager = config_manager
        self.on_save_callback = on_save_callback

        self.configure(fg_color=COLORS['bg_primary'])
        self._create_widgets()
        self._load_settings()

    def _create_widgets(self):
        """Create all settings widgets"""

        # Main container with padding
        container = ctk.CTkFrame(self, fg_color=COLORS['bg_primary'])
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # Title
        title = ctk.CTkLabel(
            container,
            text="Settings",
            font=FONTS['title'],
            text_color=COLORS['text_primary']
        )
        title.pack(anchor="w", pady=(0, 20))

        # Mail Path Section
        mail_section = ctk.CTkFrame(container, fg_color=COLORS['bg_secondary'])
        mail_section.pack(fill="x", pady=(0, 15))

        mail_label = ctk.CTkLabel(
            mail_section,
            text="SWG Mail Directory",
            font=FONTS['heading'],
            text_color=COLORS['text_primary']
        )
        mail_label.pack(anchor="w", padx=15, pady=(15, 5))

        mail_path_frame = ctk.CTkFrame(mail_section, fg_color="transparent")
        mail_path_frame.pack(fill="x", padx=15, pady=(0, 15))

        self.mail_path_entry = ctk.CTkEntry(
            mail_path_frame,
            placeholder_text="C:\\SWG Restoration III\\profiles\\character\\mail_CharacterName",
            font=FONTS['body'],
            height=35
        )
        self.mail_path_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        browse_btn = ctk.CTkButton(
            mail_path_frame,
            text="Browse",
            command=self._browse_directory,
            font=FONTS['body'],
            width=100,
            height=35
        )
        browse_btn.pack(side="right")

        # API Credentials Section
        api_section = ctk.CTkFrame(container, fg_color=COLORS['bg_secondary'])
        api_section.pack(fill="x", pady=(0, 15))

        api_label = ctk.CTkLabel(
            api_section,
            text="SWGTracker.com API Credentials",
            font=FONTS['heading'],
            text_color=COLORS['text_primary']
        )
        api_label.pack(anchor="w", padx=15, pady=(15, 5))

        # User ID
        user_id_label = ctk.CTkLabel(
            api_section,
            text="Scanner User ID",
            font=FONTS['body'],
            text_color=COLORS['text_secondary']
        )
        user_id_label.pack(anchor="w", padx=15, pady=(10, 5))

        self.user_id_entry = ctk.CTkEntry(
            api_section,
            placeholder_text="Enter your User ID",
            font=FONTS['body'],
            height=35
        )
        self.user_id_entry.pack(fill="x", padx=15, pady=(0, 10))

        # User Key
        user_key_label = ctk.CTkLabel(
            api_section,
            text="Scanner User Key (API Key)",
            font=FONTS['body'],
            text_color=COLORS['text_secondary']
        )
        user_key_label.pack(anchor="w", padx=15, pady=(5, 5))

        self.user_key_entry = ctk.CTkEntry(
            api_section,
            placeholder_text="Enter your API Key",
            font=FONTS['body'],
            show="•",
            height=35
        )
        self.user_key_entry.pack(fill="x", padx=15, pady=(0, 15))

        # Application Preferences Section
        prefs_section = ctk.CTkFrame(container, fg_color=COLORS['bg_secondary'])
        prefs_section.pack(fill="x", pady=(0, 15))

        prefs_label = ctk.CTkLabel(
            prefs_section,
            text="Application Preferences",
            font=FONTS['heading'],
            text_color=COLORS['text_primary']
        )
        prefs_label.pack(anchor="w", padx=15, pady=(15, 10))

        # Minimize to tray
        self.minimize_tray_var = ctk.BooleanVar()
        minimize_switch = ctk.CTkSwitch(
            prefs_section,
            text="Minimize to system tray",
            variable=self.minimize_tray_var,
            font=FONTS['body'],
            progress_color=COLORS['accent_green']
        )
        minimize_switch.pack(anchor="w", padx=15, pady=5)

        # Show notifications
        self.show_notifications_var = ctk.BooleanVar()
        notifications_switch = ctk.CTkSwitch(
            prefs_section,
            text="Show desktop notifications",
            variable=self.show_notifications_var,
            font=FONTS['body'],
            progress_color=COLORS['accent_green']
        )
        notifications_switch.pack(anchor="w", padx=15, pady=5)

        # Auto-start monitoring
        self.auto_start_var = ctk.BooleanVar()
        auto_start_switch = ctk.CTkSwitch(
            prefs_section,
            text="Auto-start monitoring on launch",
            variable=self.auto_start_var,
            font=FONTS['body'],
            progress_color=COLORS['accent_green']
        )
        auto_start_switch.pack(anchor="w", padx=15, pady=(5, 15))

        # Save Button
        save_btn = ctk.CTkButton(
            container,
            text="Save Settings",
            command=self._save_settings,
            font=FONTS['heading'],
            height=40,
            fg_color=COLORS['accent_green'],
            hover_color="#15803d"
        )
        save_btn.pack(fill="x", pady=(10, 0))

        # Status label
        self.status_label = ctk.CTkLabel(
            container,
            text="",
            font=FONTS['small'],
            text_color=COLORS['text_secondary']
        )
        self.status_label.pack(anchor="w", pady=(10, 0))

    def _browse_directory(self):
        """Open directory browser dialog"""
        initial_dir = self.mail_path_entry.get() or ""

        directory = filedialog.askdirectory(
            title="Select SWG Mail Directory",
            initialdir=initial_dir
        )

        if directory:
            self.mail_path_entry.delete(0, "end")
            self.mail_path_entry.insert(0, directory)

    def _load_settings(self):
        """Load settings from config manager"""
        config = self.config_manager.get_all()

        self.mail_path_entry.insert(0, config.get('mail_path', ''))
        self.user_id_entry.insert(0, config.get('scanner_user_id', ''))
        self.user_key_entry.insert(0, config.get('scanner_user_key', ''))

        self.minimize_tray_var.set(config.get('minimize_to_tray', True))
        self.show_notifications_var.set(config.get('show_notifications', True))
        self.auto_start_var.set(config.get('auto_start_monitoring', False))

    def _save_settings(self):
        """Save settings to config manager"""
        try:
            # Update config
            self.config_manager.set('mail_path', self.mail_path_entry.get())
            self.config_manager.set('scanner_user_id', self.user_id_entry.get())
            self.config_manager.set('scanner_user_key', self.user_key_entry.get())
            self.config_manager.set('minimize_to_tray', self.minimize_tray_var.get())
            self.config_manager.set('show_notifications', self.show_notifications_var.get())
            self.config_manager.set('auto_start_monitoring', self.auto_start_var.get())

            # Save to file
            if self.config_manager.save():
                self._show_status("Settings saved successfully", COLORS['success'])

                # Call callback if provided
                if self.on_save_callback:
                    self.on_save_callback()
            else:
                self._show_status("Failed to save settings", COLORS['error'])

        except Exception as e:
            logger.error(f"Error saving settings: {e}")
            self._show_status(f"Error: {str(e)}", COLORS['error'])

    def _show_status(self, message: str, color: str):
        """Show status message"""
        self.status_label.configure(text=message, text_color=color)

        # Clear status after 3 seconds
        self.after(3000, lambda: self.status_label.configure(text=""))

    def get_current_settings(self):
        """Get current settings from UI"""
        return {
            'mail_path': self.mail_path_entry.get(),
            'scanner_user_id': self.user_id_entry.get(),
            'scanner_user_key': self.user_key_entry.get(),
            'minimize_to_tray': self.minimize_tray_var.get(),
            'show_notifications': self.show_notifications_var.get(),
            'auto_start_monitoring': self.auto_start_var.get()
        }
