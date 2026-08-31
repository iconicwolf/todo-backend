from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base
from app.schemas.todo import TodoCreate, TodoUpdate

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)

def get_todos(db, completed=None):
    from sqlalchemy.orm import Session
    query = db.query(Todo)
    if completed is not None:
        query = query.filter(Todo.completed == completed)
    return query.all()

def get_todo_by_id(db, todo_id: int):
    from sqlalchemy.orm import Session
    return db.query(Todo).filter(Todo.id == todo_id).first()

def create_todo(db, todo_data: TodoCreate):
    from sqlalchemy.orm import Session
    db_todo = Todo(**todo_data.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db, todo_id: int, todo_data: TodoUpdate):
    from sqlalchemy.orm import Session
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        return None

    update_dict = todo_data.model_dump(exclude_unset=True)
    for key, value in update_dict.items():
        setattr(db_todo, key, value)

    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db, todo_id: int):
    from sqlalchemy.orm import Session
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        return False
    db.delete(db_todo)
    db.commit()
    return True
