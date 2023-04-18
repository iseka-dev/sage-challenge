from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
# from sqlalchemy.dialects.postgresql import UUID

from .database import Base


class Joke(Base):
    __tablename__ = "jokes"

    id = Column(Integer, primary_key=True, index=True)
    joke = Column(String)
