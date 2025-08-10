from fastapi import HTTPException, FastAPI
from typing import List
from Cat import CatCreate, Cat

#uvicorn 1_Main:app --reload

#curl -X POST http://127.0.0.1:8000/cats/ -H "Content-Type: application/json" -d '{"name": "Miezi", "age": 3}'
#curl http://127.0.0.1:8000/cats/
#curl http://127.0.0.1:8000/cats/1
#curl -X PUT http://127.0.0.1:8000/cats/1 -H "Content-Type: application/json" -d '{"name": "Tiger", "age": 5}'
#curl -X DELETE http://127.0.0.1:8000/cats/1


# --- FastAPI App ---
app = FastAPI()

# --- Datenbank (in-memory) ---
cats_db = []

# --- CRUD Katzen ---

@app.post("/cats/", response_model=Cat)
async def create_cat(cat: CatCreate):
    new_id = len(cats_db) + 1
    new_cat = Cat(id=new_id, **cat.dict())
    cats_db.append(new_cat)
    return new_cat

@app.get("/cats/", response_model=List[Cat])
async def read_cats():
    return cats_db

@app.get("/cats/{cat_id}", response_model=Cat)
async def read_cat(cat_id: int):
    cat = next((c for c in cats_db if c.id == cat_id), None)
    if cat is None:
        raise HTTPException(status_code=404, detail="Katze nicht gefunden")
    return cat

@app.put("/cats/{cat_id}", response_model=Cat)
async def update_cat(cat_id: int, cat_update: CatCreate):
    for index, cat in enumerate(cats_db):
        if cat.id == cat_id:
            updated_cat = Cat(id=cat_id, **cat_update.dict())
