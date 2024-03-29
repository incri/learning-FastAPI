from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID


app = FastAPI()


class BOOK(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(max_length=50, min_length=1)
    description: str = Field(max_length=100, min_length=1)
    rating: int = Field(gt=-1, lt=6)

    class Config:
        schema_extra = {
            "example": {
                "id": "UUID",
                "title": "Title Of Book",
                "author": "Author's Name",
                "description": "Description Of Book",
                "rating": 4,
            }
        }


BOOKS = []


@app.get("/")
async def books():
    return BOOKS


@app.get("/book/{id}")
async def book_detail(id: UUID):
    for book in BOOKS:
        if book.id == id:
            return book


@app.post("/")
async def create_book(book: BOOK):
    BOOKS.append(book)
    return book


