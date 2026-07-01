import requests

from .auth import get_token
from .config import BASE_URL


def get_depots():

    token = get_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"{BASE_URL}/depots",
        headers=headers
    )

    response.raise_for_status()

    return response.json()["depots"]


def get_vehicles():

    token = get_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"{BASE_URL}/vehicles",
        headers=headers
    )

    response.raise_for_status()

    return response.json()["vehicles"]