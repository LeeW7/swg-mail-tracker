"""
Utility functions for the application
"""
import sys
import os
from pathlib import Path


def get_resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller

    Args:
        relative_path: Path relative to resources directory

    Returns:
        Absolute path to the resource
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        # Running in development mode
        base_path = Path(__file__).parent

    return base_path / relative_path
