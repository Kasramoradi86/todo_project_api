from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from .. import models,schemas
from ..database import get_db

router = APIRouter(prefix="/todo_lists",tags=["Todo Lists"])

@router.post("/",response_model=schemas.TodoListResponse)
def create_todo_list(
    todo_list: schemas.TodoListCreate,
    db: Session = Depends(get_db)):
    new_list = models.TodoList(name=todo_list.name)
    db.add(new_list)
    db.commit()
    db.refresh(new_list)
    return new_list

@router.get("/",response_model= list[schemas.TodoListResponse])
def get_all_todo_lists(db:Session = Depends(get_db)):
    result = db.execute(select(models.TodoList))
    todo_lists = result.scalars().all()
    return todo_lists

@router.get("/{id}",response_model=schemas.TodoListResponse)
def get_todo_list_by_id(id:int,db:Session = Depends(get_db)):
    result = db.execute(select(models.TodoList).where(models.TodoList.id == id))
    todo_list = result.scalar_one_or_none()
    return todo_list

@router.put("/{id}",response_model=schemas.TodoListResponse)
def update_todo_list(id:int, todo_list:schemas.TodoListUpdate, db:Session = Depends(get_db)):
    existing_list = get_todo_list_by_id(id=id, db=db)
    if existing_list is not None:
        existing_list.name = todo_list.name
        db.commit()
        db.refresh(existing_list)
        return existing_list
    return None

@router.delete("/{id}")
def delete_todo_list(id:int, db:Session = Depends(get_db)):
    exising_list = get_todo_list_by_id(id=id, db=db)
    if exising_list is not None:
        db.delete(exising_list)
        db.commit()
        return {"massage":f"Todo List (id={id}) deleted"}
    return None

