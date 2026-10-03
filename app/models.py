from sqlalchemy import Boolean,String,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from .database import Base

class TodoList(Base):
    __tablename__ = "todo_lists"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[String] = mapped_column(String(100))

    todos: Mapped[list["Todo"]] = relationship(back_populates="todo_list")

class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str | None] = mapped_column(String(500),nullable=True)
    completed: Mapped[bool] = mapped_column(Boolean,default=False)

    list_id: Mapped[int] = mapped_column(ForeignKey("todo_lists.id"))
    todo_list: Mapped["TodoList"] = relationship(back_populates="todos")