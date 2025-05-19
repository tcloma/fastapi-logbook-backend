from typing import TypedDict
from fastapi import FastAPI
import json

app = FastAPI()

class Message(TypedDict):
    name: str
    content: str
    
with open('data.json', 'r') as f:
    data: list[Message] = json.load(f)

def get_message(author: str):
    for message in data:
        if author == message.get('name'):
            return message.get('content')
        
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/messages")
def get_messages():
    return data

@app.get("/messages/{author}")
def read_message(author: str):
    author = author.capitalize()
    return {"name": author, "message": f'{get_message(author)}'}