import random

from sqlalchemy.orm import Session
# from src.enums import JokeType
# from src.helpers import jokes_helpers
from src.db.schemas import JokeBase
from src.enums import JokeType
from src.exceptions import JokeNotFoundException
# from src.logger import log
from src.repositories import jokes_repo


class JokesService:
    async def get_joke(self, joke_topic: JokeType = None):
        if joke_topic is None:
            joke_topic = random.choice(list(JokeType.__members__.values()))
        if joke_topic.value == "chuck":
            joke = await jokes_repo.get_random_chuck_joke()
        elif joke_topic.value == "dad":
            joke = await jokes_repo.get_random_dad_joke()
        return JokeBase(joke=joke)

    async def create_joke(self, db: Session, joke: JokeBase):
        return await jokes_repo.create_joke(db, joke)
    
    async def get_by_id(self, id: int):
        user = await jokes_repo.get_by_id(id)
        if user is None:
            raise JokeNotFoundException(f"User '{id}' not found.")

    async def update_joke(
        self, db: Session, joke_id: int, joke: JokeBase
    ):
        joke = self.get_by_id(joke_id)
        return await jokes_repo.update_joke(db, joke_id, joke)

    async def delete_joke(
        self, db: Session, joke_id: int
    ):
        return await jokes_repo.delete_joke(db, joke_id)
