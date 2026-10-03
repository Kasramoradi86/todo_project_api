from fastapi import HTTPException,status

class TodoListNotFound(HTTPException):
    def __init__(self,id):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND,
                         detail=f"todo list (id={id}) not found")

class TodoNotFound(HTTPException):
    def __init__(self,id):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND,
                         detail=f"todo (id={id}) not found")