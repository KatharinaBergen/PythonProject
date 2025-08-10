from pydantic import BaseModel

# --- Models ---

class Cat(BaseModel):
    id: int
    name: str
    age: int

class CatCreate(BaseModel):
    name: str
    age: int
