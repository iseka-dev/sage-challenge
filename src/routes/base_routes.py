from fastapi import APIRouter
from src.routes.jokes_routes import jokes_routes


router = APIRouter()

router.include_router(jokes_routes)
