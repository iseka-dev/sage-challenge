from fastapi import FastAPI

from src.db.sql import models
from src.db.sql.database import engine
from src.db.sql.database import Base
from src.routes import base_routes
from src.settings import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(base_routes.router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(engine)
