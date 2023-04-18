from fastapi import FastAPI

from src.db.sql import models
from src.db.sql.database import engine
from src.db.sql.database import Base
from src.routes import base_routes

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="SageMakersChallenge")

app.include_router(base_routes.router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(engine)
