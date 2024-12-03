from fastapi import FastAPI
import uvicorn
from logic.logic import wiki as wiki_logic
from logic.logic import search_wiki
from logic.logic import phrase as wiki_phrases


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in wikipedia"""

    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{value}")
async def wiki(value: str):
    """Retrieve summary from wikipedia page"""
    result = wiki_logic(value)
    return {"result": result}


@app.get("/phrase/{query}")
async def phrase(query: str):
    """Retrieves the wikipedia page summary and returns phrases"""
    result = wiki_phrases(query)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="127.0.0.1")
