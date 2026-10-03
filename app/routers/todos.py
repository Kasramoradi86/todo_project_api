from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from ..database import get_db
from .. import schemas,models
from .todo_lists import get_todo_list_by_id

router = APIRouter(prefix="/todos",tags=["Todos"])

@router.post("/",response_model=schemas.TodoResponse)
def create_list(todo:schemas.TodoCreate,list_id:int, db:Session = Depends(get_db)):
    existing_list = get_todo_list_by_id(id=list_id, db=db)
    if existing_list is None:
        return None
    new_todo = models.Todo(title=todo.title, description=todo.description, completed=todo.completed, list_id=list_id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@router.get("/",response_model=list[schemas.TodoResponse])
def get_all_todos(db:Session = Depends(get_db)):
    result = db.execute(select(models.Todo))
    todos = result.scalars().all()
    return todos

@router.get("/{id}",response_model=schemas.TodoResponse)
def get_todo_by_id(id:int, db:Session = Depends(get_db)):
    existing_list = db.execute(select(models.Todo).where(models.Todo.id == id)).scalar_one_or_none()
    return existing_list

@router.put("/{id}",response_model=schemas.TodoResponse)
def update_todo(id:int, todo:schemas.TodoUpdata, db:Session = Depends(get_db)):
    existing_list = get_todo_by_id(id=id, db=db)
    if existing_list is None:
        return None
    if todo.title is not None:
        existing_list.title = todo.title
    if todo.description is not None:
        existing_list.description = todo.description
    if todo.completed is not None:
        existing_list.completed = todo.completed

    db.commit()
    db.refresh(existing_list)
    return existing_list

