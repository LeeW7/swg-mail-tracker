"""
SWG Mail Tracker - Main Application Entry Point
"""
import sys
import os
import logging
import threading
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import customtkinter as ctk
from src.core.config_manager import ConfigManager
from src.core.file_watcher import MailFileWatcher
from src.core.api_client import SWGTrackerAPI
from src.gui.main_window import MainWindow
from src.gui.system_tray import SystemTray

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('swg_mail_tracker.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class SWGMailTrackerApp:
    """Main application controller"""

    def __init__(self):
        """Initialize application"""
        self.config_manager = ConfigManager()
        self.file_watcher = None
        self.api_client = None
        self.main_window = None
        self.system_tray = None
        self.is_running = True

        logger.info("SWG Mail Tracker started")

    def start(self):
        """Start the application"""
        # Create main window
        self.main_window = MainWindow(
            config_manager=self.config_manager,
            on_start_monitoring=self.start_monitoring,
            on_stop_monitoring=self.stop_monitoring,
            on_test_connection=self.test_connection,
            on_close=self.quit_application
        )

        # Set up system tray
        self.setup_system_tray()

        # Auto-start monitoring if enabled
        if self.config_manager.get('auto_start_monitoring', False):
            self.main_window.after(1000, self._auto_start)

        # Start main loop
        self.main_window.mainloop()

    def setup_system_tray(self):
        """Set up system tray icon"""
        try:
            self.system_tray = SystemTray(
                on_show=self.show_window,
                on_hide=self.hide_window,
                on_start=lambda: self.start_monitoring(),
                on_stop=lambda: self.stop_monitoring(),
                on_exit=self.quit_application
            )

            self.system_tray.setup()

            # Run system tray in separate thread
            tray_thread = threading.Thread(
                target=self.system_tray.run,
                daemon=True
            )
            tray_thread.start()

            logger.info("System tray initialized")

        except Exception as e:
            logger.error(f"Failed to initialize system tray: {e}")

    def start_monitoring(self) -> tuple[bool, str]:
        """
        Start file monitoring

        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            # Validate configuration
            is_valid, errors = self.config_manager.validate()
            if not is_valid:
                return False, "Invalid configuration: " + ", ".join(errors)

            # Get configuration
            mail_path = self.config_manager.get('mail_path')
            user_id = self.config_manager.get('scanner_user_id')
            user_key = self.config_manager.get('scanner_user_key')

            # Create API client
            self.api_client = SWGTrackerAPI(user_id, user_key)

            # Create file watcher
            self.file_watcher = MailFileWatcher(
                watch_path=mail_path,
                callback=self.on_new_mail_file
            )

            # Start watching
            success, message = self.file_watcher.start()

            if success:
                # Update system tray
                if self.system_tray:
                    self.system_tray.update_monitoring_status(True)

                logger.info(f"Monitoring started: {mail_path}")

            return success, message

        except Exception as e:
            error_msg = f"Failed to start monitoring: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return False, error_msg

    def stop_monitoring(self) -> tuple[bool, str]:
        """
        Stop file monitoring

        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            if self.file_watcher:
                success, message = self.file_watcher.stop()

                if success:
                    # Update system tray
                    if self.system_tray:
                        self.system_tray.update_monitoring_status(False)

                    logger.info("Monitoring stopped")

                return success, message
            else:
                return False, "Monitoring is not active"

        except Exception as e:
            error_msg = f"Failed to stop monitoring: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return False, error_msg

    def on_new_mail_file(self, file_path: str):
        """
        Handle new mail file detected

        Args:
            file_path: Path to the new mail file
        """
        logger.info(f"Processing new mail file: {file_path}")

        monitor_tab = self.main_window.get_monitor_tab()

        try:
            # Update stats
            monitor_tab.update_stats('files_processed')

            # Read file content
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            if not content.strip():
                logger.warning(f"Empty file: {file_path}")
                monitor_tab.log_message(f"Skipped empty file: {os.path.basename(file_path)}", "warning")
                return

            # Send to API
            monitor_tab.log_message(f"Uploading: {os.path.basename(file_path)}", "info")

            success, message = self.api_client.send_mail_content(content)

            if success:
                monitor_tab.update_stats('files_uploaded')
                monitor_tab.log_message(f"✓ {os.path.basename(file_path)} - {message}", "success")

                # Show notification if enabled
                if self.config_manager.get('show_notifications', True):
                    self._show_notification("Mail Uploaded", f"Successfully uploaded {os.path.basename(file_path)}")

            else:
                monitor_tab.update_stats('errors')
                monitor_tab.log_message(f"✗ {os.path.basename(file_path)} - {message}", "error")

                # Show error notification if enabled
                if self.config_manager.get('show_notifications', True):
                    self._show_notification("Upload Failed", message)

        except Exception as e:
            error_msg = f"Error processing file: {str(e)}"
            logger.error(error_msg, exc_info=True)
            monitor_tab.update_stats('errors')
            monitor_tab.log_message(f"✗ {os.path.basename(file_path)} - {error_msg}", "error")

    def test_connection(self) -> tuple[bool, str]:
        """
        Test API connection

        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            # Validate configuration
            user_id = self.config_manager.get('scanner_user_id')
            user_key = self.config_manager.get('scanner_user_key')

            if not user_id or not user_key:
                return False, "User ID and API Key are required"

            # Create API client and test
            api_client = SWGTrackerAPI(user_id, user_key)
            success, message = api_client.test_connection()

            logger.info(f"Connection test: {message}")
            return success, message

        except Exception as e:
            error_msg = f"Connection test failed: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return False, error_msg

    def show_window(self):
        """Show main window"""
        if self.main_window:
            self.main_window.show_window()

    def hide_window(self):
        """Hide main window"""
        if self.main_window:
            self.main_window.hide_window()

    def quit_application(self):
        """Quit the application"""
        logger.info("Shutting down application")

        # Stop monitoring if active
        if self.file_watcher and self.file_watcher.is_active():
            self.stop_monitoring()

        # Stop system tray
        if self.system_tray:
            self.system_tray.stop()

        # Destroy window
        if self.main_window:
            self.main_window.quit()
            self.main_window.destroy()

        self.is_running = False
        sys.exit(0)

    def _auto_start(self):
        """Auto-start monitoring on launch"""
        logger.info("Auto-starting monitoring")
        success, message = self.start_monitoring()

        if success:
            self.main_window.update_monitoring_status(True)
            self.main_window.get_monitor_tab().set_monitoring_status(True, message)
            self.main_window.get_monitor_tab().log_message(f"Auto-started: {message}", "success")
        else:
            self.main_window.get_monitor_tab().log_message(f"Auto-start failed: {message}", "error")

    def _show_notification(self, title: str, message: str):
        """
        Show desktop notification (placeholder for future implementation)

        Args:
            title: Notification title
            message: Notification message
        """
        # TODO: Implement Windows notifications using win10toast or similar
        logger.info(f"Notification: {title} - {message}")


def main():
    """Main entry point"""
    try:
        app = SWGMailTrackerApp()
        app.start()
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
