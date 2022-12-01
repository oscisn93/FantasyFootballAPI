import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List
import json
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

# import the mock data as a dict from a json file.
def fetchData() -> List[Todo]:
    with open('todos.json') as file:
        todos: List[Todo] = json.load(file)
        return todos
# Instatiate the FastAPI object and set the default templates directory
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="./templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    todo_list: List[Todo] = fetchData()
    for todo in todo_list:
        title: str = todo["title"]
        todo["title"] = title.title()
    return templates.TemplateResponse("index.html", {"request": request, "todo_list": todo_list})

@app.get("/todos/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    todo: Todo = [todo for todo in fetchData() if todo["id"] == id][0]
    title: str = todo["title"]
    description: str = todo['description']
    return templates.TemplateResponse("todo.html", {"request": request, "id": id, "title": title.title(), "description": description})

@app.post("/todos", response_class=RedirectResponse)
async def add_todo(title: str = Form(), description: str = Form()):
    todos: List[Todo] = fetchData()
    todo: Todo = Todo(id=len(todos),  title=str(title), description=str(description), completed=False)
    todos.append(todo)
    with open('todos.json', 'w') as file:
        json.dump(todos, file)
    return RedirectResponse('/')

if __name__ == '__main__':
    uvicorn.run(app)
