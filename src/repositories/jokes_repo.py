import requests


async def get_random_chuck_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    return response.json()["value"]


async def get_random_dad_joke():
    headers = {"Accept": "application/json"}
    response = requests.get(
        "https://api.chucknorris.io/jokes/random", headers=headers
    )
    return response.json()["joke"]
