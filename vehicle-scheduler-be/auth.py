import httpx
from config import BASE_URL, USERNAME, PASSWORD

token = None


async def get_token():

    global token

    if token:
        return token

    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{BASE_URL}/login",
            json={
                "username": USERNAME,
                "password": PASSWORD
            }
        )

        response.raise_for_status()

        token = response.json()["token"]

        return token