from pydantic import BaseModel

class TodoListCreate(BaseModel):
    name: str

class TodoListResponse(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }

class TodoListUpdate(BaseModel):
    name: str

class TodoCreate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False
    list_id: int

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    list_id: int

    model_config = {
        "from_attributes": True
    }

class TodoUpdata(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class TodoListResponseWithTodos(TodoListResponse):
    todos: list["TodoResponse"] = []