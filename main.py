from typing import TypedDict
from fastapi import FastAPI

app = FastAPI()

class Message(TypedDict):
    name: str
    content: str
    
sampleData: list[Message] = [
    {"name": "Christye", "content": "Vivamus in felis eu sapien cursus vestibulum."},
    {"name": "Guthrie", "content": "Nulla ac enim."},
    {"name": "Mela", "content": "Sed accumsan felis."},
    {"name": "Fax", "content": "Morbi a ipsum."},
    {"name": "Liane", "content": "Suspendisse potenti."},
    {"name": "Ed", "content": "Vestibulum anteorci cubilia Curae; Duis faucibus accumsan odio."},
    {"name": "Daniella", "content": "Morbi non quam nec dui luctus rutrum."},
    {"name": "Legra", "content": "In congue."},
    {"name": "Benedetta", "content": "Vivamus vel nulla eget eros elementum pellentesque."},
    {"name": "Sada", "content": "Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla."},
]

# def get_message():
#     for message in sampleData:
#         print(message.name)
        
# get_message()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/message")
def get_messages():
    return sampleData

# @app.get("/messages/{writer}")
# def read_message(writer: str):
#     return {"name": writer, "message": ""}