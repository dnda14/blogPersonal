from datetime import datetime
import json
import markdown

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from repositories.database import Database
from controllers import endpoint


app = FastAPI()
db = Database()

app.mount("/static", StaticFiles(directory="views"))

templates = Jinja2Templates(directory="views")

with open("views/posts.json") as f:
    posts = json.load(f)

@app.get("/status")
async def health_check():
    return {"status": "OK", "timestamp": datetime.now()}

app.include_router(endpoint.router)