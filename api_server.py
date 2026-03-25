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

def format_laptops(results):

    laptops = []

    for i, title in enumerate(results[:5]):

        laptop = {
            "rank": i+1,
            "name": title,
            "cpu": "Latest Gen Processor",
            "gpu": "RTX Series GPU",
            "ram": "16GB",
            "storage": "512GB SSD",
            "display": "FHD / 144Hz",
            "reason": "Good performance in this price range"
        }

        laptops.append(laptop)

    return laptops


@app.post("/ask")
def ask(data: dict):

    query = data.get("task")

    url = f"https://news.google.com/rss/search?q={query}"

    r = requests.get(url)

    root = ET.fromstring(r.content)

    titles = []

    for item in root.findall(".//item")[:10]:
        titles.append(item.find("title").text)

    laptops = format_laptops(titles)

    return {
        "query": query,
        "result": laptops
    }
