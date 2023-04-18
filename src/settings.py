import os

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    load_dotenv()

    PROJECT_NAME = os.getenv("PROJECT_NAME", "")
    MONGO_URL = os.getenv("MONGO_URL", "")
    DB_NAME = "sage-makers-db"


settings = Settings()
