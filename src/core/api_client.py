"""
API Client for swgtracker.com communication
"""
import json
import logging
import requests
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)


class SWGTrackerAPI:
    """Handle all API communication with swgtracker.com"""

    API_URL = "https://swgtracker.com/import_mailcontent.php"
    TIMEOUT = 10  # seconds

    def __init__(self, user_key: str):
        """
        Initialize API client

        Args:
            user_key: Scanner API key
        """
        self.user_key = user_key

    def send_mail_content(self, mail_content: str) -> tuple[bool, str]:
        """
        Send mail file content to swgtracker.com

        Args:
            mail_content: Raw content of the mail file

        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            data = {
                'incomingData': mail_content,
                'scannerUserKey': self.user_key
            }

            headers = {
                'Content-type': 'application/json',
                'Accept': 'text/plain'
            }

            json_content = json.dumps(data)

            logger.debug(f"Sending mail content to {self.API_URL}")
            response = requests.post(
                self.API_URL,
                data=json_content,
                headers=headers,
                timeout=self.TIMEOUT
            )

            response.raise_for_status()

            logger.info(f"Mail content sent successfully. Status: {response.status_code}")
            return True, f"Successfully uploaded (Status: {response.status_code})"

        except requests.exceptions.Timeout:
            error_msg = "Request timed out"
            logger.error(error_msg)
            return False, error_msg

        except requests.exceptions.ConnectionError:
            error_msg = "Connection error - check your internet connection"
            logger.error(error_msg)
            return False, error_msg

        except requests.exceptions.HTTPError as e:
            error_msg = f"HTTP error: {e.response.status_code}"
            logger.error(error_msg)
            return False, error_msg

        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return False, error_msg

    def test_connection(self) -> tuple[bool, str]:
        """
        Test API connection and credentials

        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            # Send a minimal test payload
            test_data = {
                'incomingData': 'CONNECTION_TEST',
                'scannerUserKey': self.user_key
            }

            headers = {
                'Content-type': 'application/json',
                'Accept': 'text/plain'
            }

            response = requests.post(
                self.API_URL,
                data=json.dumps(test_data),
                headers=headers,
                timeout=self.TIMEOUT
            )

            if response.status_code == 200:
                return True, "Connection successful"
            else:
                return False, f"Connection failed (Status: {response.status_code})"

        except Exception as e:
            return False, f"Connection failed: {str(e)}"
