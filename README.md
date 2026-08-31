# Todo List Backend API 🚀

This project is an **agentic coding experiment** and a test-and-trial implementation of a professional REST API using **FastAPI**. It serves as a demonstration of how AI agents can architect, implement, and refine a full-stack backend with a real database and containerized infrastructure.

## 🎯 Project Goals
- Implement a clean MVC-like architecture for a Todo application.
- Transition from volatile in-memory storage to a persistent **PostgreSQL** database.
- Achieve a "Zero-Config" setup using **Docker** and **Environment Variables**.
- Demonstrate the iterative process of agentic software engineering (Refactoring $\rightarrow$ Parameterization $\rightarrow$ Stability).

## 🛠️ Technology Stack

### [FastAPI](https://fastapi.tiangolo.com/)
A modern, fast (high-performance), web framework for building APIs with Python 3.8+.
- **Key Feature Used**: Dependency Injection (`Depends`) for database session management.
- **Documentation Note**: FastAPI uses Pydantic for data validation, ensuring that the API handles input/output types strictly.

### [SQLAlchemy](https://www.sqlalchemy.org/)
The Python SQL Toolkit and Object Relational Mapper (ORM).
- **Key Feature Used**: `declarative_base` and `sessionmaker` for mapping Python classes to database tables.
- **Documentation Note**: By using an ORM, the application remains decoupled from raw SQL, making it easier to maintain and migrate.

### [PostgreSQL](https://www.postgresql.org/)
A powerful, open-source object-relational database system.
- **Configuration**: Managed via Docker to ensure a consistent environment across different machines.
- **Documentation Note**: PostgreSQL is chosen for its reliability, ACID compliance, and extensive feature set for structured data.

### [Docker & Docker Compose](https://docs.docker.com/)
Platform for developing, shipping, and running applications in containers.
- **Configuration**: 
  - `Dockerfile`: Defines the lightweight Python environment.
  - `docker-compose.yml`: Orchestrates the API, Database, and pgAdmin.
- **Documentation Note**: The use of `healthcheck` in the compose file ensures that the application only starts once the database is ready to accept connections.

## 🚀 Getting Started

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/iconicwolf/todo-backend.git
   cd todo-backend
   ```

2. **Configure Environment**:
   Copy the example environment file and update the credentials if necessary:
   ```bash
   cp .env.example .env
   ```

3. **Launch the Application**:
   ```bash
   docker-compose up --build
   ```

### Accessing the App
- **API Root**: `http://localhost:8000/`
- **Interactive API Docs (Swagger UI)**: `http://localhost:8000/docs`
- **pgAdmin (Database Management)**: `http://localhost:5050`

## 📝 Project Notes
- **Agentic Iteration**: This project was built through multiple iterations. Initially, it used an in-memory store, then moved to hardcoded DB credentials, and finally evolved into a fully parameterized system using `pydantic-settings`.
- **Stability**: The current version includes a Docker healthcheck to solve the common "database not ready" race condition during startup.
