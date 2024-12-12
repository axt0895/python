from fastapi import FastAPI

app = FastAPI()

items = [
    'Read a book',
    'Go on a walk',
    'Mediate',
    'Play Soccer'
]

@app.get("/")
def root():
    return {'Hello': 'world'}


@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    return items