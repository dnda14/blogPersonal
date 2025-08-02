from fastapi import FastAPI
from repositories.database import Database
from controllers import endpoint
from datetime import datetime


app = FastAPI()
db = Database()

@app.get("/")
async def root():
    return {"status": "OK", "message": "API funcionando"}
@app.get("/status")
async def health_check():
    return {"status": "OK", "timestamp": datetime.now()}

app.include_router(endpoint.router)