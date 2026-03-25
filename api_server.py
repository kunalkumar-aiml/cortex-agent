from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import xml.etree.ElementTree as ET

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

    url = f"https://news.google.com/rss/search?q={query}"

    r = requests.get(url)

    root = ET.fromstring(r.content)

    results = []

    for item in root.findall(".//item")[:10]:
        title = item.find("title").text
        results.append(title)

    return {
        "query": query,
        "result": results
    }
