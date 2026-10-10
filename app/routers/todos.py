from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from .. import crud
from ..exception import TodoNotFound

router = APIRouter(prefix="/todo",tags=["Todos"])

@router.post("/",response_model=schemas.TodoResponse)
def create_todo(todo:schemas.TodoCreate,db:Session = Depends(get_db)):
    return crud.create_todo(title=todo.title, description=todo.description, completed=todo.completed, db=db)

@router.get("/",response_model=list[schemas.TodoResponse])
def get_all_todos(db:Session = Depends(get_db)):
    return crud.get_all_todos(db=db)

@router.get("/{id}",response_model=schemas.TodoResponse)
def get_todo_by_id(id:int, db:Session = Depends(get_db)):
    result = crud.get_todo_by_id(id=id, db=db)
    if result is None:
        raise TodoNotFound(id)
    return result

@router.put("/",response_model=schemas.TodoResponse)
def update_todo(new_todo:schemas.TodoUpdata, db:Session = Depends(get_db)):
    result = crud.update_todo(title=new_todo.title,description=new_todo.description,completed=new_todo.completed,db=db)
    if result is None:
        raise TodoNotFound(id)
    return result

@router.delete("/")
def delete_todo(id:int, db:Session = Depends(get_db)):
    result = crud.delete_todo(id=id, db=db)
    if not result:
        raise TodoNotFound(id)
    return True





