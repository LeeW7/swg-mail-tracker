"""
File watcher for monitoring SWG mail directory
"""
import os
import time
import logging
from pathlib import Path
from typing import Callable, Optional
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent

logger = logging.getLogger(__name__)


class MailFileHandler(FileSystemEventHandler):
    """Handle file system events for mail files"""

    def __init__(self, callback: Callable[[str], None]):
        """
        Initialize file handler

        Args:
            callback: Function to call when new mail file is created
                     Takes file_path as argument
        """
        super().__init__()
        self.callback = callback

    def on_created(self, event: FileSystemEvent) -> None:
        """
        Handle file creation events

        Args:
            event: File system event
        """
        # Ignore directory events
        if event.is_directory:
            return

        file_path = event.src_path
        logger.info(f"New file detected: {file_path}")

        # Small delay to ensure file is fully written
        time.sleep(0.1)

        # Call the callback with the file path
        try:
            self.callback(file_path)
        except Exception as e:
            logger.error(f"Error in file callback: {e}", exc_info=True)


class MailFileWatcher:
    """Watch for new mail files in SWG directory"""

    def __init__(self, watch_path: str, callback: Callable[[str], None]):
        """
        Initialize file watcher

        Args:
            watch_path: Directory path to watch
            callback: Function to call when new mail file is created
        """
        self.watch_path = watch_path
        self.callback = callback
        self.observer: Optional[Observer] = None
        self.is_running = False

    def start(self) -> tuple[bool, str]:
        """
        Start watching the directory

        Returns:
            Tuple of (success: bool, message: str)
        """
        if self.is_running:
            return False, "Watcher is already running"

        # Validate watch path
        if not os.path.exists(self.watch_path):
            error_msg = f"Watch path does not exist: {self.watch_path}"
            logger.error(error_msg)
            return False, error_msg

        if not os.path.isdir(self.watch_path):
            error_msg = f"Watch path is not a directory: {self.watch_path}"
            logger.error(error_msg)
            return False, error_msg

        try:
            # Create observer and handler
            self.observer = Observer()
            event_handler = MailFileHandler(self.callback)

            # Schedule the observer
            self.observer.schedule(
                event_handler,
                self.watch_path,
                recursive=True
            )

            # Start the observer
            self.observer.start()
            self.is_running = True

            logger.info(f"Started watching: {self.watch_path}")
            return True, f"Monitoring started: {self.watch_path}"

        except Exception as e:
            error_msg = f"Failed to start watcher: {str(e)}"
            logger.error(error_msg, exc_info=True)
            self.is_running = False
            return False, error_msg

    def stop(self) -> tuple[bool, str]:
        """
        Stop watching the directory

        Returns:
            Tuple of (success: bool, message: str)
        """
        if not self.is_running:
            return False, "Watcher is not running"

        try:
            if self.observer:
                self.observer.stop()
                self.observer.join(timeout=5)
                self.observer = None

            self.is_running = False
            logger.info("Stopped watching")
            return True, "Monitoring stopped"

        except Exception as e:
            error_msg = f"Error stopping watcher: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return False, error_msg

    def is_active(self) -> bool:
        """
        Check if watcher is currently active

        Returns:
            True if watching, False otherwise
        """
        return self.is_running and self.observer is not None
