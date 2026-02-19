from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class Item(BaseModel):
    id: Optional[int]
    title: str
    description: Optional[str] = None


_db: List[Item] = []
_next_id = 1


def _get_item_index(item_id: int) -> int:
    for i, it in enumerate(_db):
        if it.id == item_id:
            return i
    return -1


@app.get("/items", response_model=List[Item])
def list_items():
    return _db


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    idx = _get_item_index(item_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Item not found")
    return _db[idx]


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    global _next_id
    item.id = _next_id
    _next_id += 1
    _db.append(item)
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    idx = _get_item_index(item_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Item not found")
    updated.id = item_id
    _db[idx] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    idx = _get_item_index(item_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Item not found")
    _db.pop(idx)
    return
