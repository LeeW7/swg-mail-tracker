"""
System tray integration
"""
import pystray
from PIL import Image, ImageDraw
import logging
from typing import Callable, Optional

logger = logging.getLogger(__name__)


class SystemTray:
    """System tray icon and menu"""

    def __init__(
        self,
        on_show: Callable,
        on_hide: Callable,
        on_start: Callable,
        on_stop: Callable,
        on_exit: Callable
    ):
        """
        Initialize system tray

        Args:
            on_show: Callback to show main window
            on_hide: Callback to hide main window
            on_start: Callback to start monitoring
            on_stop: Callback to stop monitoring
            on_exit: Callback to exit application
        """
        self.on_show = on_show
        self.on_hide = on_hide
        self.on_start = on_start
        self.on_stop = on_stop
        self.on_exit = on_exit

        self.icon: Optional[pystray.Icon] = None
        self.is_monitoring = False

    def create_icon(self):
        """Create system tray icon"""
        try:
            # Try to load the logo from resources
            from pathlib import Path
            icon_path = Path(__file__).parent.parent / "resources" / "icon.png"

            if icon_path.exists():
                image = Image.open(icon_path)
                # Resize to system tray size if needed
                image = image.resize((64, 64), Image.Resampling.LANCZOS)
                return image
        except Exception as e:
            logger.warning(f"Could not load logo for system tray: {e}")

        # Fallback: Create a simple icon (green circle on dark background)
        width = 64
        height = 64
        image = Image.new('RGB', (width, height), (10, 15, 10))
        draw = ImageDraw.Draw(image)

        # Draw green circle
        draw.ellipse([12, 12, 52, 52], fill=(22, 163, 74), outline=(255, 255, 255))

        return image

    def setup(self):
        """Set up system tray icon"""
        try:
            icon_image = self.create_icon()

            # Create menu
            menu = pystray.Menu(
                pystray.MenuItem(
                    "Show",
                    self._handle_show,
                    default=True
                ),
                pystray.MenuItem(
                    "Start Monitoring",
                    self._handle_start,
                    visible=lambda item: not self.is_monitoring
                ),
                pystray.MenuItem(
                    "Stop Monitoring",
                    self._handle_stop,
                    visible=lambda item: self.is_monitoring
                ),
                pystray.Menu.SEPARATOR,
                pystray.MenuItem(
                    "Exit",
                    self._handle_exit
                )
            )

            # Create icon
            self.icon = pystray.Icon(
                "SWGMailTracker",
                icon_image,
                "SWG Mail Tracker",
                menu
            )

            logger.info("System tray icon created")

        except Exception as e:
            logger.error(f"Error creating system tray icon: {e}")

    def run(self):
        """Run system tray (blocking call)"""
        if self.icon:
            try:
                self.icon.run()
            except Exception as e:
                logger.error(f"Error running system tray: {e}")

    def stop(self):
        """Stop system tray"""
        if self.icon:
            try:
                self.icon.stop()
                logger.info("System tray stopped")
            except Exception as e:
                logger.error(f"Error stopping system tray: {e}")

    def update_monitoring_status(self, is_monitoring: bool):
        """
        Update monitoring status

        Args:
            is_monitoring: Whether monitoring is active
        """
        self.is_monitoring = is_monitoring

        # Update icon if needed
        if self.icon:
            self.icon.update_menu()

    def _handle_show(self, icon, item):
        """Handle show window"""
        self.on_show()

    def _handle_start(self, icon, item):
        """Handle start monitoring"""
        self.on_start()

    def _handle_stop(self, icon, item):
        """Handle stop monitoring"""
        self.on_stop()

    def _handle_exit(self, icon, item):
        """Handle exit application"""
        self.on_exit()
