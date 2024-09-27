from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    id: int = None
    name: str
    price: int


app = FastAPI()

items = [
    {
        "id": 0,
        "name": "NVIDIA GeForce RTX 4090",
        "price": 3999
    },
    {
        "id": 1,
        "name": "AMD RX590",
        "price": 199
    },
    {
        "id": 2,
        "name": "Intel i9-19900K",
        "price": 27999
    },
    {
        "id": 3,
        "name": "ASUS PRIME B750",
        "price": 6599
    },
    {
        "id": 4,
        "name": "AMD RX7900K",
        "price": 8999
    },
]


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/items/")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item


@app.post("/items/")
def create_item(new_item: Item):
    if not new_item.id:
        new_id = items[-1]['id'] + 1
    else:
        new_id = new_item.id
    items.append(
        {"id": new_id, 'name': new_item.name, 'price': new_item.price}
    )
    return items[-1]
