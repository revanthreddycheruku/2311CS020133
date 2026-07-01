import time
import requests

from app.config import (
    BASE_URL,
    EMAIL,
    NAME,
    ROLLNO,
    ACCESSCODE,
    CLIENTID,
    CLIENTSECRET
)

# Store token and expiry globally
access_token = None
expiry_time = 0


def get_token():
    """
    Returns a valid Bearer token.
    Reuses the token until it expires, then fetches a new one.
    """

    global access_token
    global expiry_time

    # Reuse existing token if still valid
    if access_token and time.time() < expiry_time:
        return access_token

    url = f"{BASE_URL}/auth"

    payload = {
        "email": EMAIL,
        "name": NAME,
        "rollNo": ROLLNO,
        "accessCode": ACCESSCODE,
        "clientID": CLIENTID,
        "clientSecret": CLIENTSECRET
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()

        data = response.json()

        access_token = data["access_token"]

        # expires_in is a Unix timestamp
        expiry_time = data["expires_in"] - 10

        return access_token

    except requests.exceptions.RequestException as e:
        raise Exception(f"Authentication failed: {e}")