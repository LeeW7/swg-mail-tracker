"""
Configuration manager for the application
"""
import json
import os
import logging
from pathlib import Path
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


class ConfigManager:
    """Manage application configuration"""

    DEFAULT_CONFIG = {
        "mail_path": "",
        "scanner_user_id": "",
        "scanner_user_key": "",
        "start_with_windows": False,
        "minimize_to_tray": True,
        "show_notifications": True,
        "auto_start_monitoring": False
    }

    def __init__(self, config_file: str = "config.json"):
        """
        Initialize configuration manager

        Args:
            config_file: Path to configuration file
        """
        self.config_file = Path(config_file)
        self.config: Dict[str, Any] = {}
        self.load()

    def load(self) -> bool:
        """
        Load configuration from file

        Returns:
            True if successful, False otherwise
        """
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded_config = json.load(f)

                # Merge with defaults to ensure all keys exist
                self.config = {**self.DEFAULT_CONFIG, **loaded_config}
                logger.info(f"Configuration loaded from {self.config_file}")
                return True
            else:
                logger.info("No config file found, using defaults")
                self.config = self.DEFAULT_CONFIG.copy()
                return False

        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config file: {e}")
            self.config = self.DEFAULT_CONFIG.copy()
            return False

        except Exception as e:
            logger.error(f"Error loading config: {e}")
            self.config = self.DEFAULT_CONFIG.copy()
            return False

    def save(self) -> bool:
        """
        Save current configuration to file

        Returns:
            True if successful, False otherwise
        """
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)

            logger.info(f"Configuration saved to {self.config_file}")
            return True

        except Exception as e:
            logger.error(f"Error saving config: {e}")
            return False

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value

        Args:
            key: Configuration key
            default: Default value if key doesn't exist

        Returns:
            Configuration value or default
        """
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Set configuration value

        Args:
            key: Configuration key
            value: Value to set
        """
        self.config[key] = value

    def get_all(self) -> Dict[str, Any]:
        """
        Get all configuration values

        Returns:
            Dictionary of all configuration
        """
        return self.config.copy()

    def validate(self) -> tuple[bool, list[str]]:
        """
        Validate current configuration

        Returns:
            Tuple of (is_valid: bool, errors: list[str])
        """
        errors = []

        # Check mail path
        mail_path = self.get("mail_path", "")
        if not mail_path:
            errors.append("Mail path is required")
        elif not os.path.exists(mail_path):
            errors.append(f"Mail path does not exist: {mail_path}")

        # Check user credentials
        if not self.get("scanner_user_id"):
            errors.append("Scanner User ID is required")

        if not self.get("scanner_user_key"):
            errors.append("Scanner User Key is required")

        is_valid = len(errors) == 0
        return is_valid, errors

    def import_from_old_config(self, old_config_path: str) -> bool:
        """
        Import configuration from old config.txt format

        Args:
            old_config_path: Path to old config.txt file

        Returns:
            True if successful, False otherwise
        """
        try:
            import configparser

            parser = configparser.ConfigParser()
            parser.read(old_config_path)

            if parser.has_section('swg-scanner'):
                self.set('scanner_user_id', parser.get('swg-scanner', 'scannerUserID', fallback=''))
                self.set('scanner_user_key', parser.get('swg-scanner', 'scannerUserKey', fallback=''))
                self.set('mail_path', parser.get('swg-scanner', 'mailPath', fallback=''))

                logger.info(f"Imported configuration from {old_config_path}")
                return True

        except Exception as e:
            logger.error(f"Error importing old config: {e}")

        return False
