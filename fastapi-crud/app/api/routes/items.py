from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.repositories.item_repo import get_item, create_item, update_item, delete_item
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/items/", response_model=Item)
def create_item_view(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)

@router.get("/items/{item_id}", response_model=Item)
def read_item_view(item_id: int, db: Session = Depends(get_db)):
    db_item = get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/items/{item_id}", response_model=Item)
def update_item_view(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    db_item = get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return update_item(db, db_item, item)

@router.delete("/items/{item_id}", response_model=dict)
def delete_item_view(item_id: int, db: Session = Depends(get_db)):
    db_item = get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    delete_item(db, db_item)
    return {"ok": True}
