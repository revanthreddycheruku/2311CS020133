import httpx

from auth import get_token
from config import BASE_URL


async def get_vehicles():

    token = await get_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{BASE_URL}/vehicles",
            headers=headers
        )

        response.raise_for_status()

        return response.json()["vehicles"]


async def get_depots():

    token = await get_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{BASE_URL}/depots",
            headers=headers
        )

        response.raise_for_status()

        return response.json()["depots"]