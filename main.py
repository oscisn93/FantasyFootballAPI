""" Main Module for our todo application """
import json
from typing import List
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn


class User(BaseModel):
    """ User Model """
    username: str
    email: str
    password: str


class Todo(BaseModel):
    """ Todo Model """
    id: int
    title: str
    description: str
    completed: bool


# import the mock data as a dict from a json file.
def fetch_data() -> List[Todo]:
    """ fetch todo data """
    with open('todos.json', encoding='json') as file:
        todos: List[Todo] = json.load(file)
        return todos
# Instatiate the FastAPI object and set the default templates directory
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    """ root route """
    return {"message": "Hello World"}

@app.get("/todos")
async def get_todos():
    """ get all todos """
    return fetch_data()


@app.post("/todos/{id}")
async def create_todo(todo: Todo):
    """ create a new todo """
    return todo

if __name__ == "__main__":
    uvicorn.run(app)
