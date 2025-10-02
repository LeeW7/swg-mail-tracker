from requests import Request, Session
import json
import logging
import requests

def send_mailContent(mailContent):
    """
    Send mail content to swgtracker.com

    Args:
        mailContent: JSON string containing mail data

    Returns:
        Response object from the API
    """
    headers = { 'Content-type': 'application/json', 'Accept': 'text/plain' }
    r = requests.post('https://swgtracker.com/import_mailcontent.php', data=mailContent, headers=headers)
    return r
