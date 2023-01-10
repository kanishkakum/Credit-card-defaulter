import pandas as pd
import pymongo
import json
from dataclasses import dataclass
import os

@dataclass()
class EnviornmentVariable():
    mongo_db_url:str= os.getenv("MONGO_DB_URL")

env_var=EnviornmentVariable
client = pymongo.MongoClient(env_var.mongo_db_url)