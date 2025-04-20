# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests<3",
#     "rich",
# ]
# ///
import requests
from rich.pretty import pprint
from fastapi import FastAPI
from .routers import items

response = requests.get("https://peps.python.org/api/peps.json")
data = response.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])

app = FastAPI()
app.include_router(items.router)


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


# ... 다른 라우터 및 로직 ...
