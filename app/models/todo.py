from typing import List, Optional, Dict
from app.schemas.todo import TodoRead, TodoCreate, TodoUpdate

class TodoDB:
    def __init__(self):
        self._db: Dict[int, TodoRead] = {}
        self._id_counter = 1

    def get_all(self, completed: Optional[bool] = None) -> List[TodoRead]:
        if completed is None:
            return list(self._db.values())
        return [todo for todo in self._db.values() if todo.completed == completed]

    def get_by_id(self, todo_id: int) -> Optional[TodoRead]:
        return self._db.get(todo_id)

    def create(self, todo_data: TodoCreate) -> TodoRead:
        todo_id = self._id_counter
        new_todo = TodoRead(id=todo_id, **todo_data.model_dump())
        self._db[todo_id] = new_todo
        self._id_counter += 1
        return new_todo

    def update(self, todo_id: int, todo_data: TodoUpdate) -> Optional[TodoRead]:
        if todo_id not in self._db:
            return None

        current_todo = self._db[todo_id]
        update_data = todo_data.model_dump(exclude_unset=True)

        # Create a new TodoRead with updated fields
        updated_todo = current_todo.model_copy(update=update_data)
        self._db[todo_id] = updated_todo
        return updated_todo

    def delete(self, todo_id: int) -> bool:
        if todo_id in self._db:
            del self._db[todo_id]
            return True
        return False

# Singleton instance for the in-memory database
todo_db = TodoDB()
