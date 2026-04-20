from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routes import items

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(items.router)
