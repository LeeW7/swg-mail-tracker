"""
Settings tab for configuration management
"""
import customtkinter as ctk
from tkinter import filedialog
import logging
from typing import Callable, List, Dict
from .theme import COLORS, FONTS

logger = logging.getLogger(__name__)


class MailPathEntry(ctk.CTkFrame):
    """Individual mail path entry widget"""

    def __init__(self, master, index: int, on_remove: Callable, **kwargs):
        """
        Initialize mail path entry

        Args:
            master: Parent widget
            index: Entry index (0-3)
            on_remove: Callback when remove button is clicked
        """
        super().__init__(master, fg_color="transparent", **kwargs)
        self.index = index
        self.on_remove = on_remove

        # Character label entry
        label_frame = ctk.CTkFrame(self, fg_color="transparent")
        label_frame.pack(fill="x", pady=(10, 5))

        label_text = ctk.CTkLabel(
            label_frame,
            text=f"Character {index + 1} Name (optional)",
            font=FONTS['body'],
            text_color=COLORS['text_secondary']
        )
        label_text.pack(side="left")

        self.label_entry = ctk.CTkEntry(
            label_frame,
            placeholder_text="e.g., Main Tank, Trader, etc.",
            font=FONTS['body'],
            height=35,
            width=250
        )
        self.label_entry.pack(side="right")

        # Path entry with browse and remove buttons
        path_frame = ctk.CTkFrame(self, fg_color="transparent")
        path_frame.pack(fill="x", pady=(0, 5))

        self.path_entry = ctk.CTkEntry(
            path_frame,
            placeholder_text="C:\\SWG Restoration III\\profiles\\character\\mail_CharacterName",
            font=FONTS['body'],
            height=35
        )
        self.path_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        browse_btn = ctk.CTkButton(
            path_frame,
            text="Browse",
            command=self._browse_directory,
            font=FONTS['body'],
            width=80,
            height=35
        )
        browse_btn.pack(side="left", padx=(0, 5))

        # Remove button (only show for entries after the first)
        if index > 0:
            remove_btn = ctk.CTkButton(
                path_frame,
                text="×",
                command=lambda: on_remove(self),
                font=('Segoe UI', 20, 'bold'),
                width=35,
                height=35,
                fg_color=COLORS['accent_red'],
                hover_color="#b91c1c"
            )
            remove_btn.pack(side="left")

    def _browse_directory(self):
        """Open directory browser dialog"""
        initial_dir = self.path_entry.get() or ""

        directory = filedialog.askdirectory(
            title="Select SWG Mail Directory",
            initialdir=initial_dir
        )

        if directory:
            self.path_entry.delete(0, "end")
            self.path_entry.insert(0, directory)

    def get_values(self) -> Dict[str, str]:
        """Get current values"""
        return {
            "path": self.path_entry.get().strip(),
            "label": self.label_entry.get().strip()
        }

    def set_values(self, path: str, label: str):
        """Set values"""
        self.path_entry.delete(0, "end")
        self.path_entry.insert(0, path)
        self.label_entry.delete(0, "end")
        self.label_entry.insert(0, label)


class SettingsTab(ctk.CTkFrame):
    """Settings configuration tab"""

    MAX_MAIL_PATHS = 4

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
        self.mail_path_entries: List[MailPathEntry] = []

        self.configure(fg_color=COLORS['bg_primary'])
        self._create_widgets()
        self._load_settings()

    def _create_widgets(self):
        """Create all settings widgets"""

        # Create scrollable frame
        scrollable_frame = ctk.CTkScrollableFrame(
            self,
            fg_color=COLORS['bg_primary'],
            scrollbar_button_color=COLORS['bg_tertiary'],
            scrollbar_button_hover_color=COLORS['border']
        )
        scrollable_frame.pack(fill="both", expand=True, padx=0, pady=0)

        # Main container inside scrollable frame with padding
        container = ctk.CTkFrame(scrollable_frame, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=20, pady=(10, 20))

        # Title
        title = ctk.CTkLabel(
            container,
            text="Settings",
            font=FONTS['title'],
            text_color=COLORS['text_primary']
        )
        title.pack(anchor="w", pady=(0, 10))

        # Mail Paths Section
        mail_section = ctk.CTkFrame(container, fg_color=COLORS['bg_secondary'])
        mail_section.pack(fill="x", pady=(0, 10))

        # Section header
        header_frame = ctk.CTkFrame(mail_section, fg_color="transparent")
        header_frame.pack(fill="x", padx=15, pady=(10, 5))

        mail_label = ctk.CTkLabel(
            header_frame,
            text="SWG Mail Directories (up to 4 characters)",
            font=FONTS['heading'],
            text_color=COLORS['text_primary']
        )
        mail_label.pack(side="left")

        # Container for mail path entries
        self.mail_paths_container = ctk.CTkFrame(mail_section, fg_color="transparent")
        self.mail_paths_container.pack(fill="x", padx=15, pady=(0, 10))

        # Add initial entry
        self._add_mail_path_entry()

        # Add Character button
        self.add_button = ctk.CTkButton(
            mail_section,
            text="+ Add Character",
            command=self._add_mail_path_entry,
            font=FONTS['body'],
            height=35,
            fg_color=COLORS['bg_tertiary'],
            hover_color=COLORS['border'],
            border_width=1,
            border_color=COLORS['border']
        )
        self.add_button.pack(padx=15, pady=(5, 15))

        # API Credentials Section
        api_section = ctk.CTkFrame(container, fg_color=COLORS['bg_secondary'])
        api_section.pack(fill="x", pady=(0, 10))

        api_label = ctk.CTkLabel(
            api_section,
            text="SWGTracker.com API Key",
            font=FONTS['heading'],
            text_color=COLORS['text_primary']
        )
        api_label.pack(anchor="w", padx=15, pady=(10, 5))

        # API Key
        user_key_label = ctk.CTkLabel(
            api_section,
            text="API Key",
            font=FONTS['body'],
            text_color=COLORS['text_secondary']
        )
        user_key_label.pack(anchor="w", padx=15, pady=(10, 5))

        self.user_key_entry = ctk.CTkEntry(
            api_section,
            placeholder_text="Enter your API Key",
            font=FONTS['body'],
            show="•",
            height=35
        )
        self.user_key_entry.pack(fill="x", padx=15, pady=(0, 10))

        # Application Preferences Section
        prefs_section = ctk.CTkFrame(container, fg_color=COLORS['bg_secondary'])
        prefs_section.pack(fill="x", pady=(0, 10))

        prefs_label = ctk.CTkLabel(
            prefs_section,
            text="Application Preferences",
            font=FONTS['heading'],
            text_color=COLORS['text_primary']
        )
        prefs_label.pack(anchor="w", padx=15, pady=(10, 8))

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
        auto_start_switch.pack(anchor="w", padx=15, pady=(5, 10))

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
        save_btn.pack(fill="x", pady=(5, 0))

        # Status label
        self.status_label = ctk.CTkLabel(
            container,
            text="",
            font=FONTS['small'],
            text_color=COLORS['text_secondary']
        )
        self.status_label.pack(anchor="w", pady=(10, 0))

    def _add_mail_path_entry(self):
        """Add a new mail path entry"""
        if len(self.mail_path_entries) >= self.MAX_MAIL_PATHS:
            self._show_status(f"Maximum {self.MAX_MAIL_PATHS} characters allowed", COLORS['error'])
            return

        index = len(self.mail_path_entries)
        entry = MailPathEntry(
            self.mail_paths_container,
            index=index,
            on_remove=self._remove_mail_path_entry
        )
        entry.pack(fill="x", pady=(0, 10))
        self.mail_path_entries.append(entry)

        # Disable add button if at max
        if len(self.mail_path_entries) >= self.MAX_MAIL_PATHS:
            self.add_button.configure(state="disabled")

    def _remove_mail_path_entry(self, entry: MailPathEntry):
        """Remove a mail path entry"""
        if entry in self.mail_path_entries:
            self.mail_path_entries.remove(entry)
            entry.destroy()

            # Re-index remaining entries
            for i, e in enumerate(self.mail_path_entries):
                e.index = i

            # Re-enable add button
            if len(self.mail_path_entries) < self.MAX_MAIL_PATHS:
                self.add_button.configure(state="normal")

    def _load_settings(self):
        """Load settings from config manager"""
        config = self.config_manager.get_all()

        # Load mail paths
        mail_paths = config.get('mail_paths', [])
        if mail_paths:
            # Clear default entry
            for entry in self.mail_path_entries:
                entry.destroy()
            self.mail_path_entries.clear()

            # Add entries for each saved path
            for i, mail_entry in enumerate(mail_paths):
                if i >= self.MAX_MAIL_PATHS:
                    break

                self._add_mail_path_entry()
                if isinstance(mail_entry, dict):
                    path = mail_entry.get("path", "")
                    label = mail_entry.get("label", "")
                    self.mail_path_entries[i].set_values(path, label)

        # Load API key
        self.user_key_entry.insert(0, config.get('scanner_user_key', ''))

        # Load preferences
        self.minimize_tray_var.set(config.get('minimize_to_tray', True))
        self.show_notifications_var.set(config.get('show_notifications', True))
        self.auto_start_var.set(config.get('auto_start_monitoring', False))

    def _save_settings(self):
        """Save settings to config manager"""
        try:
            # Collect mail paths from entries
            mail_paths = []
            for entry in self.mail_path_entries:
                values = entry.get_values()
                # Only save if path is not empty
                if values["path"]:
                    mail_paths.append(values)

            # Update config
            self.config_manager.set('mail_paths', mail_paths)
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
        # Collect mail paths from entries
        mail_paths = []
        for entry in self.mail_path_entries:
            values = entry.get_values()
            if values["path"]:
                mail_paths.append(values)

        return {
            'mail_paths': mail_paths,
            'scanner_user_key': self.user_key_entry.get(),
            'minimize_to_tray': self.minimize_tray_var.get(),
            'show_notifications': self.show_notifications_var.get(),
            'auto_start_monitoring': self.auto_start_var.get()
        }
