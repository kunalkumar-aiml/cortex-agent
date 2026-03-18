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
def root():
    return {"message": "Cortex AI Agent Running"}

@app.post("/ask")
def ask(data: dict):

    query = data.get("task")

    url = f"https://duckduckgo.com/html/?q={query}"

    headers = {
        "User-Agent":"Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text,"html.parser")

    results = []

    for a in soup.select(".result__a")[:10]:
        results.append(a.get_text())

    return {"result":results}
