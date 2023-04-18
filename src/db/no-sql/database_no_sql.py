from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from src.logger import log


uri = "https://sa-east-1.aws.data.mongodb-api.com/"\
    "app/data-fzeyr/endpoint/data/v1"

# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))
