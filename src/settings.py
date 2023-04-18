import os

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    load_dotenv()

    PROJECT_NAME = os.getenv("PROJECT_NAME", "")


settings = Settings()
