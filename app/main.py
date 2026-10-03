from fastapi import FastAPI
from .database import engine,Base
from . import models
from .routers import todo_lists,todos

Base.metadata.create_all(bind=engine)

app = FastAPI(description="a simple system built with fastapi to manage todo lists")

app.include_router(todo_lists.router)
app.include_router(todos.router)