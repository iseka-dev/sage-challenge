from fastapi import APIRouter
from src.routes.jokes_routes import jokes_routes
from src.routes.nums_routes import nums_routes


router = APIRouter()

router.include_router(jokes_routes)
router.include_router(nums_routes)
