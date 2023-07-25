from fastapi import FastAPI
from enum import Enum

app = FastAPI()

BOOKS = {
    "book_1": {"title": "Title One", "author": "Author One"},
    "book_2": {"title": "Title Two", "author": "Author Two"},
    "book_3": {"title": "Title Three", "author": "Author Three"},
    "book_4": {"title": "Title Four", "author": "Author Four"},
    "book_5": {"title": "Title Five", "author": "Author Five"},
}


class DirectionName(str, Enum):
    north = "North"
    south = "south"
    east = "East"
    west = "west"


@app.get("/")
async def books():
    return BOOKS


@app.get("/books/{id}")
async def book_detail(id: int):
    return {"id": id}


@app.get("/directions/{direction_name}")
async def direction_detail(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "up"}
    if direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub": "Down"}

    if direction_name == DirectionName.west:
        return {"Direction": direction_name, "sub": "Left"}
    return {"Direction": direction_name, "sub": "Right"}
