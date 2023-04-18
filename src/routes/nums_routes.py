from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Path
from fastapi import status
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.schemas import JokeBase
from src.enums import JokeType
from src.logger import log
from src.services.nums_services import NumsService


nums_routes = APIRouter(
    prefix="/nums",
    tags=["nums"]
)


@nums_routes.get("/", status_code=status.HTTP_200_OK)
async def get_lower_common_multiple(nums: list(int)):
    """
    Get a random joke.
    """
    try:
        return await NumsService().get_lower_common_multiple(nums)
    except Exception as e:
        log.error(f"Error detail: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={f"Error detail: {e}"},
        )