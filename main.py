from fastapi import FastAPI
from pydantic import BaseModel
import json

class User(BaseModel):
    username: str
    email: str
    password: str

class Todo(BaseModel):
    id: int
    title: str
    description: str
    owner: str
    completed: bool
    edited: bool

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/todos")
async def get_todos():
    with open('todos.json') as todos:
        data = json.load(todos)
        return data

@app.post("/todos/{id}")
async def create_todo(todo: Todo):
    return todo