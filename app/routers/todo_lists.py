from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from .. import models,schemas
from ..database import get_db
from ..exception import TodoListNotFound
from .. import crud

router = APIRouter(prefix="/todo_lists",tags=["Todo Lists"])

@router.post("/",response_model=schemas.TodoListResponse)
def create_todo_list(
    todo_list: schemas.TodoListCreate,
    db: Session = Depends(get_db)):
    return crud.create_todo_list(name=todo_list.name,db=db)

@router.get("/",response_model= list[schemas.TodoListResponse])
def get_all_todo_lists(db:Session = Depends(get_db)):
    return crud.get_all_todo_lists(db=db)


@router.get("/{id}",response_model=schemas.TodoListResponse)
def get_todo_list_by_id(id:int,db:Session = Depends(get_db)):
    result = crud.get_todo_list_by_id(id=id, db=db)
    if result is None:
        raise TodoListNotFound(id)
    return result

@router.put("/{id}",response_model=schemas.TodoListResponse)
def update_todo_list(id:int, new_todo_list:schemas.TodoListUpdate, db:Session = Depends(get_db)):
    result = crud.update_todo_list(id=id,new_name=new_todo_list.name, db=db)
    if result is None:
        raise TodoListNotFound(id)
    return result

@router.delete("/{id}")
def delete_todo_list(id:int, db:Session = Depends(get_db)):
    result = crud.delete_todo_list(id=id, db=db)
    if not result:
        raise TodoListNotFound(id)
    return result


@router.get("/{id}/todos",response_model=list[schemas.TodoResponse])
def get_todo_list_with_todos(id:int, db:Session = Depends(get_db)):
    return crud.get_todo_list_with_todos(list_id=id, db=db)



       
