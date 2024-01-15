from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
async def index():
    return {"Data": "hello"}


# http://127.0.0.1:8000/countries/japan
@app.get("/countries/{country_name}")
async def country(country_name):
    return {"国名": country_name}


# http://127.0.0.1:8000/search/World
# {"ID":1,"タイトル":null,"内容":"World"}


# http://127.0.0.1:8000/search/Hello?id=2&title=TTT
# {"ID":2,"タイトル":"TTT","内容":"Hello"}
@app.get("/search/{description}")
async def searchPage(
    id: int = 1, title: Optional[str] = None, description: str = "存在しなません"
):
    return {
        "ID": id,
        "タイトル": title,
        "内容": description,
    }

