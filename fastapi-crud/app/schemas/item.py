from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str = ""

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class ItemInDBBase(ItemBase):
    id: int
    class Config:
        orm_mode = True

class Item(ItemInDBBase):
    pass
