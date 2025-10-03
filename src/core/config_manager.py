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
        "mail_paths": [],  # List of {"path": str, "label": str}
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

                # Migrate old mail_path to new mail_paths format
                self._migrate_mail_path()

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

        # Check mail paths - at least one valid path required
        mail_paths = self.get("mail_paths", [])
        if not mail_paths:
            errors.append("At least one mail directory is required")
        else:
            valid_paths = 0
            for i, mail_entry in enumerate(mail_paths):
                if isinstance(mail_entry, dict):
                    path = mail_entry.get("path", "")
                    if path and os.path.exists(path):
                        valid_paths += 1
                    elif path:
                        errors.append(f"Mail path {i+1} does not exist: {path}")

            if valid_paths == 0:
                errors.append("At least one valid mail directory is required")

        # Check API key
        if not self.get("scanner_user_key"):
            errors.append("API Key is required")

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
                self.set('scanner_user_key', parser.get('swg-scanner', 'scannerUserKey', fallback=''))

                # Import old mail_path as first entry in mail_paths
                old_path = parser.get('swg-scanner', 'mailPath', fallback='')
                if old_path:
                    self.set('mail_paths', [{"path": old_path, "label": ""}])

                logger.info(f"Imported configuration from {old_config_path}")
                return True

        except Exception as e:
            logger.error(f"Error importing old config: {e}")

        return False

    def _migrate_mail_path(self) -> None:
        """
        Migrate old mail_path (string) to new mail_paths (list) format
        """
        # Check if old mail_path exists and mail_paths is empty
        if "mail_path" in self.config and not self.config.get("mail_paths"):
            old_path = self.config.get("mail_path", "")
            if old_path:
                self.config["mail_paths"] = [{"path": old_path, "label": ""}]
                logger.info(f"Migrated old mail_path to mail_paths format")

            # Remove old mail_path key
            del self.config["mail_path"]
