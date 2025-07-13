from fastapi import FastAPI
from .repositories.database import Database




app = FastAPI()
db = Database()

