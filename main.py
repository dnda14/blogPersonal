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

@app.get("/",response_class=HTMLResponse)
async def root(request: Request):
    #return {"status": "OK", "message": "API funcionando"}
    return templates.TemplateResponse("index.html", {"request":request, "posts":posts})

@app.get("/post/{slug}")
def show_post(request: Request, slug: str):
    path = f"posts/{slug}.md"
    with open(path, "r", encoding="utf-8") as f:
        content = markdown.markdown(f.read(), extensions=["fenced_code", "codehilite"])
    return templates.TemplateResponse("post.html", {"request": request, "content": content})


@app.get("/status")
async def health_check():
    return {"status": "OK", "timestamp": datetime.now()}

app.include_router(endpoint.router)