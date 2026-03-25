from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Cortex AI Agent Running"}

@app.post("/ask")
def ask(data: dict):

    query = data.get("task")

    url = "https://html.duckduckgo.com/html/"

    params = {
        "q": query
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, params=params, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    results = []

    links = soup.find_all("a")

    for link in links:

        text = link.get_text()

        if text and len(text) > 30:
            results.append(text)

        if len(results) == 10:
            break

    return {
        "query": query,
        "result": results
    }
