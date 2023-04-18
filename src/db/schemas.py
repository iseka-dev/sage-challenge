from pydantic import BaseModel

from src.enums import JokeType


class JokeBase(BaseModel):
    joke: str

    class Config:
        schema_extra = {
            "example": {
                "joke": "place your joke here",
            }
        }


class JokeTypeRequest(BaseModel):
    name: JokeType
