from typing import TypedDict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(TypedDict):
    name: str
    content: str

data: list[Message]
 
# grab data on initial load
with open('data.json', 'r') as f:
    data = json.load(f)
    f.close()
        
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/messages")
def get_messages():
    return data

@app.post("/messages")
async def create_message(message: Message):
    with open('data.json', 'w') as f:
        data.append(message)
        json.dump(data, f, indent=4)
        f.close()
    return data