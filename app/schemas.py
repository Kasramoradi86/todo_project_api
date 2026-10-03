from pydantic import BaseModel

class TodoListCreate(BaseModel):
    name: str

class TodoListResponse(BaseModel):
    id: int
    name: str

class TodoCreate(BaseModel):
    title: str
    description: str | None = None

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    list_id: int