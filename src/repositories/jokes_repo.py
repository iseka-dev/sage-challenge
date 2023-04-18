import requests

from src.db.sql.models import Joke
from src.logger import log


async def get_random_chuck_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    return response.json()["value"]


async def get_random_dad_joke():
    headers = {"Accept": "application/json"}
    response = await requests.get(
        "https://icanhazdadjoke.com/", headers=headers
    )
    return response.json()["joke"]


async def create_joke(db, joke):
    new_joke = Joke(joke=joke.joke)
    db.add(new_joke)
    db.commit()
    db.refresh(new_joke)
    return {
        "Created_joke_id": new_joke.id,
        "joke": new_joke.joke
    }


def update_joke(db, joke_id, joke):
    update_joke = db.query(Joke).get(joke_id)
    if update_joke:
        update_joke.joke = joke.joke
        db.commit()
        db.refresh(update_joke)
        return {update_joke.id, update_joke.joke}
    else:
        return {"There is no joke with that ID"}


def delete_joke(db, joke_id):
    delete_joke = db.query(Joke).get(joke_id)
    if delete_joke:
        db.delete(delete_joke)
        db.commit()
        log.debug("heeeereeeeee", delete_joke)
        return {"Done"}
    else:
        return {"There is no joke with that ID"}
