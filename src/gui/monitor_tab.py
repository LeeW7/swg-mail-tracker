"""
Monitor tab for real-time status and activity log
"""
import customtkinter as ctk
from datetime import datetime
import logging
from typing import Optional
from .theme import COLORS, FONTS

logger = logging.getLogger(__name__)


class MonitorTab(ctk.CTkFrame):
    """Monitoring and status tab"""

    def __init__(self, master, config_manager):
        """
        Initialize monitor tab

        Args:
            master: Parent widget
            config_manager: ConfigManager instance
        """
        super().__init__(master)
        self.config_manager = config_manager
        self.is_monitoring = False
        self.stats = {
            'files_processed': 0,
            'files_uploaded': 0,
            'errors': 0,
            'start_time': None
        }

        self.configure(fg_color=COLORS['bg_primary'])
        self._create_widgets()

    def _create_widgets(self):
        """Create all monitor widgets"""

        # Main container
        container = ctk.CTkFrame(self, fg_color=COLORS['bg_primary'])
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # Title
        title = ctk.CTkLabel(
            container,
            text="Monitor",
            font=FONTS['title'],
            text_color=COLORS['text_primary']
        )
        title.pack(anchor="w", pady=(0, 20))

        # Status Section
        status_section = ctk.CTkFrame(container, fg_color=COLORS['bg_secondary'])
        status_section.pack(fill="x", pady=(0, 15))

        status_title = ctk.CTkLabel(
            status_section,
            text="Status",
            font=FONTS['heading'],
            text_color=COLORS['text_primary']
        )
        status_title.pack(anchor="w", padx=15, pady=(15, 10))

        # Status indicator
        status_frame = ctk.CTkFrame(status_section, fg_color="transparent")
        status_frame.pack(fill="x", padx=15, pady=(0, 15))

        self.status_indicator = ctk.CTkLabel(
            status_frame,
            text="●",
            font=('Segoe UI', 24),
            text_color=COLORS['text_muted']
        )
        self.status_indicator.pack(side="left", padx=(0, 10))

        self.status_text = ctk.CTkLabel(
            status_frame,
            text="Not Monitoring",
            font=FONTS['body'],
            text_color=COLORS['text_secondary']
        )
        self.status_text.pack(side="left")

        # Statistics Section
        stats_section = ctk.CTkFrame(container, fg_color=COLORS['bg_secondary'])
        stats_section.pack(fill="x", pady=(0, 15))

        stats_title = ctk.CTkLabel(
            stats_section,
            text="Statistics",
            font=FONTS['heading'],
            text_color=COLORS['text_primary']
        )
        stats_title.pack(anchor="w", padx=15, pady=(15, 10))

        # Stats grid
        stats_grid = ctk.CTkFrame(stats_section, fg_color="transparent")
        stats_grid.pack(fill="x", padx=15, pady=(0, 15))

        # Files Processed
        processed_frame = ctk.CTkFrame(stats_grid, fg_color=COLORS['bg_tertiary'])
        processed_frame.pack(side="left", expand=True, fill="both", padx=(0, 10))

        ctk.CTkLabel(
            processed_frame,
            text="Files Processed",
            font=FONTS['small'],
            text_color=COLORS['text_secondary']
        ).pack(pady=(10, 5))

        self.processed_label = ctk.CTkLabel(
            processed_frame,
            text="0",
            font=('Segoe UI', 20, 'bold'),
            text_color=COLORS['text_primary']
        )
        self.processed_label.pack(pady=(0, 10))

        # Files Uploaded
        uploaded_frame = ctk.CTkFrame(stats_grid, fg_color=COLORS['bg_tertiary'])
        uploaded_frame.pack(side="left", expand=True, fill="both", padx=(0, 10))

        ctk.CTkLabel(
            uploaded_frame,
            text="Successfully Uploaded",
            font=FONTS['small'],
            text_color=COLORS['text_secondary']
        ).pack(pady=(10, 5))

        self.uploaded_label = ctk.CTkLabel(
            uploaded_frame,
            text="0",
            font=('Segoe UI', 20, 'bold'),
            text_color=COLORS['success']
        )
        self.uploaded_label.pack(pady=(0, 10))

        # Errors
        errors_frame = ctk.CTkFrame(stats_grid, fg_color=COLORS['bg_tertiary'])
        errors_frame.pack(side="left", expand=True, fill="both")

        ctk.CTkLabel(
            errors_frame,
            text="Errors",
            font=FONTS['small'],
            text_color=COLORS['text_secondary']
        ).pack(pady=(10, 5))

        self.errors_label = ctk.CTkLabel(
            errors_frame,
            text="0",
            font=('Segoe UI', 20, 'bold'),
            text_color=COLORS['error']
        )
        self.errors_label.pack(pady=(0, 10))

        # Activity Log Section
        log_section = ctk.CTkFrame(container, fg_color=COLORS['bg_secondary'])
        log_section.pack(fill="both", expand=True)

        log_header = ctk.CTkFrame(log_section, fg_color="transparent")
        log_header.pack(fill="x", padx=15, pady=(15, 10))

        log_title = ctk.CTkLabel(
            log_header,
            text="Activity Log",
            font=FONTS['heading'],
            text_color=COLORS['text_primary']
        )
        log_title.pack(side="left")

        clear_btn = ctk.CTkButton(
            log_header,
            text="Clear Log",
            command=self._clear_log,
            font=FONTS['small'],
            width=80,
            height=25,
            fg_color=COLORS['bg_tertiary'],
            hover_color=COLORS['border']
        )
        clear_btn.pack(side="right")

        # Activity log textbox
        self.log_textbox = ctk.CTkTextbox(
            log_section,
            font=FONTS['mono'],
            wrap="word",
            state="disabled",
            fg_color=COLORS['bg_tertiary']
        )
        self.log_textbox.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        # Configure text tags for colored output
        self.log_textbox.tag_config("info", foreground=COLORS['info'])
        self.log_textbox.tag_config("success", foreground=COLORS['success'])
        self.log_textbox.tag_config("error", foreground=COLORS['error'])
        self.log_textbox.tag_config("warning", foreground=COLORS['warning'])
        self.log_textbox.tag_config("timestamp", foreground=COLORS['text_muted'])

    def set_monitoring_status(self, is_monitoring: bool, message: str = ""):
        """
        Update monitoring status

        Args:
            is_monitoring: Whether monitoring is active
            message: Optional status message
        """
        self.is_monitoring = is_monitoring

        if is_monitoring:
            self.status_indicator.configure(text_color=COLORS['success'])
            self.status_text.configure(
                text=message or "Monitoring Active",
                text_color=COLORS['success']
            )
            if self.stats['start_time'] is None:
                self.stats['start_time'] = datetime.now()
        else:
            self.status_indicator.configure(text_color=COLORS['text_muted'])
            self.status_text.configure(
                text=message or "Not Monitoring",
                text_color=COLORS['text_secondary']
            )

    def log_message(self, message: str, level: str = "info"):
        """
        Add message to activity log

        Args:
            message: Message to log
            level: Log level (info, success, error, warning)
        """
        timestamp = datetime.now().strftime("%H:%M:%S")

        self.log_textbox.configure(state="normal")
        self.log_textbox.insert("end", f"[{timestamp}] ", "timestamp")
        self.log_textbox.insert("end", f"{message}\n", level)
        self.log_textbox.configure(state="disabled")
        self.log_textbox.see("end")

    def update_stats(self, stat_type: str, increment: int = 1):
        """
        Update statistics

        Args:
            stat_type: Type of stat to update (files_processed, files_uploaded, errors)
            increment: Amount to increment by
        """
        if stat_type in self.stats:
            self.stats[stat_type] += increment

            # Update UI
            if stat_type == 'files_processed':
                self.processed_label.configure(text=str(self.stats['files_processed']))
            elif stat_type == 'files_uploaded':
                self.uploaded_label.configure(text=str(self.stats['files_uploaded']))
            elif stat_type == 'errors':
                self.errors_label.configure(text=str(self.stats['errors']))

    def reset_stats(self):
        """Reset all statistics"""
        self.stats = {
            'files_processed': 0,
            'files_uploaded': 0,
            'errors': 0,
            'start_time': None
        }

        self.processed_label.configure(text="0")
        self.uploaded_label.configure(text="0")
        self.errors_label.configure(text="0")

    def _clear_log(self):
        """Clear activity log"""
        self.log_textbox.configure(state="normal")
        self.log_textbox.delete("1.0", "end")
        self.log_textbox.configure(state="disabled")
        logger.info("Activity log cleared")

    def get_stats(self):
        """Get current statistics"""
        return self.stats.copy()
