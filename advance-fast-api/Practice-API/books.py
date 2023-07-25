from typing import Optional
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

BOOKS = {
    "book_1": {"id": 1, "title": "Title One", "author": "Author One"},
    "book_2": {"id": 2, "title": "Title Two", "author": "Author Two"},
    "book_3": {"id": 3, "title": "Title Three", "author": "Author Three"},
    "book_4": {"id": 4, "title": "Title Four", "author": "Author Four"},
    "book_5": {"id": 5, "title": "Title Five", "author": "Author Five"},
}


@app.get("/")
async def books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/{book_name}")
async def book_detail(book_name: str):
    return BOOKS[book_name]
