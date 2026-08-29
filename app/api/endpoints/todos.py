from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.schemas.todo import TodoRead, TodoCreate, TodoUpdate
from app.models.todo import todo_db

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.get("/", response_model=List[TodoRead])
async def read_todos(completed: Optional[bool] = Query(None)):
    """Retrieve all todo items, optionally filtered by completion status."""
    return todo_db.get_all(completed)

@router.get("/{todo_id}", response_model=TodoRead)
async def read_todo(todo_id: int):
    """Retrieve a specific todo item by ID."""
    todo = todo_db.get_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return todo

@router.post("/", response_model=TodoRead, status_code=201)
async def create_todo(todo: TodoCreate):
    """Create a new todo item."""
    return todo_db.create(todo)

@router.put("/{todo_id}", response_model=TodoRead)
async def update_todo(todo_id: int, todo: TodoUpdate):
    """Update an existing todo item."""
    updated_todo = todo_db.update(todo_id, todo)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return updated_todo

@router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    """Delete a todo item."""
    success = todo_db.delete(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return {"message": "Todo item deleted successfully"}
