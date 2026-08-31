from fastapi import FastAPI
from app.api.endpoints import todos
from app.db import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo List API",
    description="A professional Todo List backend using MVC architecture",
    version="1.0.0"
)

# Include the todo router
app.include_router(todos.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Todo List API. Visit /docs for API documentation."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
