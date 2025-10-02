"""
Main application window
"""
import customtkinter as ctk
import logging
from typing import Optional
from .theme import COLORS, FONTS
from .settings_tab import SettingsTab
from .monitor_tab import MonitorTab

logger = logging.getLogger(__name__)


class MainWindow(ctk.CTk):
    """Main application window"""

    def __init__(
        self,
        config_manager,
        on_start_monitoring,
        on_stop_monitoring,
        on_test_connection,
        on_close
    ):
        """
        Initialize main window

        Args:
            config_manager: ConfigManager instance
            on_start_monitoring: Callback to start monitoring
            on_stop_monitoring: Callback to stop monitoring
            on_test_connection: Callback to test API connection
            on_close: Callback when window is closed
        """
        super().__init__()

        self.config_manager = config_manager
        self.on_start_monitoring = on_start_monitoring
        self.on_stop_monitoring = on_stop_monitoring
        self.on_test_connection = on_test_connection
        self.on_close_callback = on_close

        self.is_monitoring = False

        self._setup_window()
        self._create_widgets()

    def _setup_window(self):
        """Set up main window properties"""
        self.title("SWG Mail Tracker")
        self.geometry("900x700")

        # Set minimum size
        self.minsize(800, 600)

        # Set window icon
        try:
            import os
            from pathlib import Path
            icon_path = Path(__file__).parent.parent / "resources" / "icon.png"
            if icon_path.exists():
                from PIL import Image
                icon_image = Image.open(icon_path)
                self.iconphoto(True, ctk.CTkImage(light_image=icon_image, dark_image=icon_image, size=(32, 32))._light_image)
        except Exception as e:
            logger.warning(f"Could not load window icon: {e}")

        # Set theme colors
        self.configure(fg_color=COLORS['bg_primary'])

        # Set appearance mode
        ctk.set_appearance_mode("dark")
        ctk.deactivate_automatic_dpi_awareness()  # May help with theme widget

        # Handle window close
        self.protocol("WM_DELETE_WINDOW", self._on_window_close)

    def _create_widgets(self):
        """Create all widgets"""

        # Header
        header = ctk.CTkFrame(self, fg_color=COLORS['bg_secondary'], height=80)
        header.pack(fill="x", padx=0, pady=0)
        header.pack_propagate(False)

        # Logo (left side of header)
        try:
            from pathlib import Path
            from PIL import Image
            icon_path = Path(__file__).parent.parent / "resources" / "icon.png"
            if icon_path.exists():
                logo_image = Image.open(icon_path)
                logo_ctk = ctk.CTkImage(light_image=logo_image, dark_image=logo_image, size=(50, 50))
                logo_label = ctk.CTkLabel(header, image=logo_ctk, text="")
                logo_label.pack(side="left", padx=(20, 10), pady=15)
        except Exception as e:
            logger.warning(f"Could not load header logo: {e}")

        # Title and subtitle
        title_frame = ctk.CTkFrame(header, fg_color="transparent")
        title_frame.pack(side="left", padx=(10, 20), pady=15)

        app_title = ctk.CTkLabel(
            title_frame,
            text="SWG Mail Tracker",
            font=('Segoe UI', 20, 'bold'),
            text_color=COLORS['text_primary']
        )
        app_title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            title_frame,
            text="Sync Star Wars Galaxies mail to swgtracker.com",
            font=FONTS['small'],
            text_color=COLORS['text_secondary']
        )
        subtitle.pack(anchor="w")

        # Control buttons
        controls_frame = ctk.CTkFrame(header, fg_color="transparent")
        controls_frame.pack(side="right", padx=20, pady=15)

        self.start_button = ctk.CTkButton(
            controls_frame,
            text="Start Monitoring",
            command=self._handle_start,
            font=FONTS['body'],
            width=140,
            height=35,
            fg_color=COLORS['accent_green'],
            hover_color="#15803d"
        )
        self.start_button.pack(side="left", padx=(0, 10))

        self.stop_button = ctk.CTkButton(
            controls_frame,
            text="Stop Monitoring",
            command=self._handle_stop,
            font=FONTS['body'],
            width=140,
            height=35,
            state="disabled"
        )
        self.stop_button.pack(side="left", padx=(0, 10))

        self.test_button = ctk.CTkButton(
            controls_frame,
            text="Test Connection",
            command=self._handle_test,
            font=FONTS['body'],
            width=140,
            height=35,
            fg_color=COLORS['bg_tertiary'],
            hover_color=COLORS['border'],
            border_width=1,
            border_color=COLORS['border']
        )
        self.test_button.pack(side="left")

        # Tab view
        self.tabview = ctk.CTkTabview(
            self,
            fg_color=COLORS['bg_primary'],
            segmented_button_fg_color=COLORS['bg_secondary'],
            segmented_button_selected_color=COLORS['accent_red'],
            segmented_button_selected_hover_color="#b91c1c"
        )
        self.tabview.pack(fill="both", expand=True, padx=0, pady=0)

        # Create tabs
        self.tabview.add("Monitor")
        self.tabview.add("Settings")

        # Monitor tab
        self.monitor_tab = MonitorTab(
            self.tabview.tab("Monitor"),
            self.config_manager
        )
        self.monitor_tab.pack(fill="both", expand=True)

        # Settings tab
        self.settings_tab = SettingsTab(
            self.tabview.tab("Settings"),
            self.config_manager,
            on_save_callback=self._on_settings_saved
        )
        self.settings_tab.pack(fill="both", expand=True)

        # Set default tab
        self.tabview.set("Monitor")

    def _handle_start(self):
        """Handle start monitoring button"""
        # Validate configuration first
        is_valid, errors = self.config_manager.validate()

        if not is_valid:
            error_msg = "Configuration errors:\n" + "\n".join(f"• {err}" for err in errors)
            self.monitor_tab.log_message(error_msg, "error")
            self.tabview.set("Settings")
            return

        # Call start callback
        success, message = self.on_start_monitoring()

        if success:
            self.is_monitoring = True
            self.start_button.configure(state="disabled")
            self.stop_button.configure(state="normal")
            self.monitor_tab.set_monitoring_status(True, message)
            self.monitor_tab.log_message(message, "success")
        else:
            self.monitor_tab.log_message(f"Failed to start: {message}", "error")

    def _handle_stop(self):
        """Handle stop monitoring button"""
        success, message = self.on_stop_monitoring()

        if success:
            self.is_monitoring = False
            self.start_button.configure(state="normal")
            self.stop_button.configure(state="disabled")
            self.monitor_tab.set_monitoring_status(False, message)
            self.monitor_tab.log_message(message, "info")
        else:
            self.monitor_tab.log_message(f"Failed to stop: {message}", "error")

    def _handle_test(self):
        """Handle test connection button"""
        self.monitor_tab.log_message("Testing connection...", "info")

        # Disable button during test
        self.test_button.configure(state="disabled")

        # Run test in separate thread to avoid blocking UI
        def test_thread():
            success, message = self.on_test_connection()

            # Update UI on main thread
            self.after(0, lambda: self._handle_test_result(success, message))

        import threading
        threading.Thread(target=test_thread, daemon=True).start()

    def _handle_test_result(self, success: bool, message: str):
        """Handle test connection result"""
        self.test_button.configure(state="normal")

        if success:
            self.monitor_tab.log_message(message, "success")
        else:
            self.monitor_tab.log_message(f"Connection test failed: {message}", "error")

    def _on_settings_saved(self):
        """Handle settings saved event"""
        self.monitor_tab.log_message("Settings saved successfully", "success")

    def _on_window_close(self):
        """Handle window close event"""
        # Check if minimize to tray is enabled
        if self.config_manager.get('minimize_to_tray', True):
            self.withdraw()  # Hide window instead of closing
            logger.info("Window minimized to tray")
        else:
            self.on_close_callback()

    def show_window(self):
        """Show the window"""
        self.deiconify()
        self.lift()
        self.focus_force()

    def hide_window(self):
        """Hide the window"""
        self.withdraw()

    def get_monitor_tab(self) -> MonitorTab:
        """Get monitor tab reference"""
        return self.monitor_tab

    def get_settings_tab(self) -> SettingsTab:
        """Get settings tab reference"""
        return self.settings_tab

    def update_monitoring_status(self, is_monitoring: bool):
        """Update monitoring status from external source"""
        self.is_monitoring = is_monitoring

        if is_monitoring:
            self.start_button.configure(state="disabled")
            self.stop_button.configure(state="normal")
        else:
            self.start_button.configure(state="normal")
            self.stop_button.configure(state="disabled")
