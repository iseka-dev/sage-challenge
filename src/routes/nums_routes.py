from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query
from fastapi import status

from src.logger import log
from src.services.nums_services import NumsService


nums_routes = APIRouter(
    prefix="/nums",
    tags=["nums"]
)


@nums_routes.get("/lcm/", status_code=status.HTTP_200_OK)
async def get_lower_common_multiple(
    nums: list[int] = Query(...)
):
    """
    Get Lower Common multiple for an array of integers.
    """
    try:
        log.debug(nums)
        return NumsService().get_lower_common_multiple(nums)
    except Exception as e:
        log.error(f"Error detail: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={f"Error detail: {e}"},
        )


@nums_routes.get("/next/", status_code=status.HTTP_200_OK)
async def next_number(nums: int = Query(...)):
    """
    Get Lower Common multiple for an array of integers.
    """
    try:
        return NumsService().next_mumber(nums)
    except Exception as e:
        log.error(f"Error detail: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={f"Error detail: {e}"},
        )
