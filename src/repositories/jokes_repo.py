import requests

from bson.objectid import ObjectId
from fastapi import HTTPException
from fastapi import Request
from sqlalchemy.orm import Session
from src.db.schemas import JokeBase
from src.db.sql.models import Joke
from src.logger import log


async def get_random_chuck_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    return response.json()["value"]


async def get_random_dad_joke():
    headers = {
        "Accept": "application/json",
        "User-Agent": "https://github.com/iseka-dev/sage-makers-challenge"
    }
    response = requests.get(
        "https://icanhazdadjoke.com/", headers=headers
    )
    return response.json()["joke"]


async def create_joke(db: Session, joke: JokeBase):
    new_joke = Joke(joke=joke.joke)
    db.add(new_joke)
    db.commit()
    db.refresh(new_joke)
    return {
        "Created_joke_id": new_joke.id,
        "joke": new_joke.joke
    }


def update_joke(db: Session, joke_id: int, joke: JokeBase):
    update_joke = db.query(Joke).get(joke_id)
    if update_joke:
        update_joke.joke = joke.joke
        db.commit()
        db.refresh(update_joke)
        return {update_joke.id, update_joke.joke}
    else:
        return {"There is no joke with that ID"}


def delete_joke(db: Session, joke_id: int):
    delete_joke = db.query(Joke).get(joke_id)
    if delete_joke:
        db.delete(delete_joke)
        db.commit()
        return {"Done"}
    else:
        return {"There is no joke with that ID"}


async def create_mongo_joke(request: Request, joke: JokeBase):
    joke = joke.dict()
    collection = request.app.mongo_database.jokes
    activity = collection.insert_one(joke)
    return({
        f"Joke created at Mongo - ID: {activity.inserted_id}"
    })


async def update_mongo_joke(request: Request, id: str, joke: JokeBase):
    obj_id = ObjectId(id)
    collection = request.app.mongo_database.jokes
    coll_obj = collection.find_one_and_update(
        {"_id": obj_id},
        {"$set": {
            "joke": joke.joke
        }}
    )
    if coll_obj:
        return(f"Updated object - id: {id}, joke: {joke.joke}")
    return "There is no object with that ID"


async def delete_mongo_joke(request: Request, id: str):
    obj_id = ObjectId(id)
    collection = request.app.mongo_database.jokes
    coll_obj = collection.delete_one({"_id": obj_id})
    if coll_obj:
        return(f"Deleted object - id: {id}")
    return("There is no object with that ID")
