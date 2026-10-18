from sqlalchemy.orm import Session
from sqlalchemy import select
from .. import models


def create_todo_list(name:str, db:Session):
    todo_list = models.TodoList(name=name)
    db.add(todo_list)
    db.commit()
    db.refresh(todo_list)
    return todo_list

def get_all_todo_lists(db:Session):
    result = db.execute(select(models.TodoList))
    return result.scalars().all()

def get_todo_list_by_id(id:int, db:Session):
    result = db.get(models.TodoList,id)
    return result

def get_todo_list_with_todos(list_id:int, db:Session):
    existing_list = get_todo_list_by_id(id=list_id, db=db)
    if existing_list is None:
        return None
    return existing_list.todos

def get_todo_list_stat(list_id:int, db=Session):
    todos = get_todo_list_with_todos(list_id=list_id, db=db)
    if todos is None:
        return None
    all_counter = len(todos)
    completed_counter = sum(todo.completed for todo in todos)
    uncompleted_counter = all_counter - completed_counter
    return {"all":all_counter,"completed":completed_counter,"uncompleted":uncompleted_counter}


def update_todo_list(id:int, new_name:str, db:Session):

    result = db.get(models.TodoList,id)
    if result is None:
        return None
    result.name = new_name
    db.commit()
    db.refresh(result)
    return result

def delete_todo_list(id:int, db:Session):
    result = get_todo_list_by_id(id=id, db=db)
    if result is None:
        return False
    db.delete(result)
    db.commit()
    return True