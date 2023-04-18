from fastapi import FastAPI
import pymongo

from src.db.sql import models
from src.db.sql.database import engine
from src.db.sql.database import Base
from src.logger import log
from src.routes import base_routes
from src.settings import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(base_routes.router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(engine)


@app.on_event("startup")
async def startup_event():
    app.mongodb_client = pymongo.MongoClient(settings.MONGO_URL)
    app.mongo_database = app.mongodb_client[settings.DB_NAME]
    try:
        app.mongodb_client.admin.command('ping')
        log.debug("Successfully connected to MongoDB!")
    except Exception as e:
        log.debug(e)
