from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Path
from fastapi import Request
from fastapi import status
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.schemas import JokeBase
from src.enums import JokeType
from src.logger import log
from src.services.jokes_services import JokesService


jokes_routes = APIRouter(
    prefix="/jokes",
    tags=["jokes"]
)


@jokes_routes.get("/", status_code=status.HTTP_200_OK)
async def get_random_joke():
    """
    Get a random joke.
    """
    try:
        return await JokesService().get_joke()
    except Exception as e:
        log.error(f"Error detail: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={f"Error detail: {e}"},
        )


@jokes_routes.get("/{joke_source}", status_code=status.HTTP_200_OK)
async def get_joke_from_source(joke_source: Annotated[
        JokeType, Path(
            title="Joke source",
            description="The source where the joke comes from"
        )
]):
    """
    Get a joke from one of our third party providers
    (chuck & dads at the moment)!
    """
    try:
        return await JokesService().get_joke(joke_source)
    except Exception as e:
        log.error(f"Error detail: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={f"Error detail: {e}"}
        )


@jokes_routes.post("/", status_code=status.HTTP_200_OK)
async def create_joke(request: Request, joke: JokeBase, db: Session = Depends(get_db)):
    """
    Stores a joke in the db
    """
    try:
        await JokesService().create_mongo_joke(request, joke)
        return await JokesService().create_joke(db, joke)
    except Exception as e:
        log.error(f"Error detail: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={f"Error detail: {e}"}
        )


@jokes_routes.put("/jokes/{joke_id}")
async def update_joke(
    joke_id: int, joke: JokeBase, db: Session = Depends(get_db)
):
    """
    Updates a joke in the db
    """
    try:
        return await JokesService().update_joke(db, joke_id, joke)
    except Exception as e:
        log.error(f"Error detail: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={f"Error detail: {e}"}
        )


@jokes_routes.delete("/jokes/{joke_id}")
async def delete_joke(
    joke_id: int, db: Session = Depends(get_db)
):
    """
    Deletes a joke from the db
    """
    try:
        return await JokesService().delete_joke(db, joke_id)
    except Exception as e:
        log.error(f"Error detail: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={f"Error detail: {e}"}
        )


@jokes_routes.post("/mongo", status_code=status.HTTP_200_OK)
async def create_mongo_joke(request: Request, joke: JokeBase):
    """
    Stores a joke in the mongo db
    """
    try:
        return await JokesService().create_mongo_joke(request, joke)
    except Exception as e:
        log.error(f"Error detail: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={f"Error detail: {e}"}
        )


@jokes_routes.put("/mongo", status_code=status.HTTP_200_OK)
async def update_mongo_joke(request: Request, id: str, joke: JokeBase):
    """
    Updates a joke in the mongo db
    """
    try:
        return await JokesService().update_mongo_joke(request, id, joke)
    except Exception as e:
        log.error(f"Error detail: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={f"Error detail: {e}"}
        )

@jokes_routes.delete("/mongo", status_code=status.HTTP_200_OK)
async def delete_mongo_joke(request: Request, id: str):
    """
    Updates a joke in the mongo db
    """
    try:
        return await JokesService().delete_mongo_joke(request, id)
    except Exception as e:
        log.error(f"Error detail: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={f"Error detail: {e}"}
        )
