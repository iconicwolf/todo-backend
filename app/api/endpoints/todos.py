from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List, Optional
from sqlalchemy.orm import Session
from app.schemas.todo import TodoRead, TodoCreate, TodoUpdate
from app.db import get_db
from app.models import todo as todo_crud

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.get("/", response_model=List[TodoRead])
async def read_todos(completed: Optional[bool] = Query(None), db: Session = Depends(get_db)):
    """Retrieve all todo items, optionally filtered by completion status."""
    return todo_crud.get_todos(db, completed)

@router.get("/{todo_id}", response_model=TodoRead)
async def read_todo(todo_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific todo item by ID."""
    todo = todo_crud.get_todo_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return todo

@router.post("/", response_model=TodoRead, status_code=201)
async def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    """Create a new todo item."""
    return todo_crud.create_todo(db, todo)

@router.put("/{todo_id}", response_model=TodoRead)
async def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    """Update an existing todo item."""
    updated_todo = todo_crud.update_todo(db, todo_id, todo)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return updated_todo

@router.delete("/{todo_id}")
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a todo item."""
    success = todo_crud.delete_todo(db, todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return {"message": "Todo item deleted successfully"}
