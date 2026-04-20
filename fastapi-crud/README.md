# FastAPI CRUD App - Project Structure Explanation

This project demonstrates a modular FastAPI CRUD application using SQLAlchemy and Pydantic. Below is a detailed explanation of each folder and file:

## Folders & Files

### app/main.py
- **Entry point** for the FastAPI application.
- Initializes the app and includes API routers.

### app/core/database.py
- Sets up the **SQLAlchemy database engine, session, and base class**.
- Central place for DB connection configuration.

### app/models/item.py
- Contains the **SQLAlchemy ORM model** for the `Item` entity.
- Defines the table structure for items in the database.

### app/schemas/item.py
- Contains **Pydantic schemas** for request and response validation.
- Defines `ItemBase`, `ItemCreate`, `ItemUpdate`, and `Item` schemas.

### app/repositories/item_repo.py
- Contains **CRUD operations** for the `Item` model.
- Functions to create, read, update, and delete items in the database.

### app/api/routes/items.py
- Defines the **API endpoints** for item CRUD operations.
- Uses repository functions and schemas for request/response handling.

### app/api/deps.py
- Dependency functions (e.g., `get_db`) for use in API routes.
- Ensures proper database session management.

### app/api/routes/
- Folder for organizing different API route files (e.g., items, users, etc.).

### app/core/
- Core application configuration (database, settings, etc.).

### app/models/
- All SQLAlchemy ORM models go here.

### app/schemas/
- All Pydantic schemas for data validation and serialization.

### app/repositories/
- Data access layer: CRUD logic for each model.

### app/services/ (empty)
- For business logic or service classes (not used in this simple CRUD example).

### app/utils/ (empty)
- For utility/helper functions.

### app/middleware/ (empty)
- For custom middleware (e.g., authentication, logging).

---

## How it works
- **main.py** starts the app and includes routers.
- **Routes** handle HTTP requests and use **schemas** for validation.
- **Repositories** interact with the **models** and the database.
- **Database** config is centralized in `core/database.py`.

You can extend this structure by adding more models, schemas, repositories, and routes as your app grows.
