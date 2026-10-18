from sqlalchemy.orm import Session
from sqlalchemy import select
from .. import models
from .todo_list import get_todo_list_by_id

def create_todo(title:str, description:str, completed:bool,todo_list_id:int, db:Session):
    todo_list = get_todo_list_by_id(id=todo_list_id, db=db)
    if todo_list is None:
        return None
    todo = models.Todo(title=title, description=description, completed=completed, list_id=todo_list_id)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def get_all_todos(db:Session):
    result = db.execute(select(models.Todo))
    return result.scalars().all()

def get_todo_by_id(id:int, db:Session):
    return db.get(models.Todo,id)

def update_todo(id:int, title:str, description:str, completed:bool, db:Session):
    todo = get_todo_by_id(id=id, db=db)
    if todo is None:
        return None
    if title is not None:
        todo.title = title
    if description is not None:
        todo.description = description
    if completed is not None:
        todo.completed = completed
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(id:int, db:Session):
    result = get_todo_by_id(id=id,db=db)
    if result is None:
        return False
    db.delete(result)
    db.commit()
    return True