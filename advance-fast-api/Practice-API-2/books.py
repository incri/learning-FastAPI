from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID

app = FastAPI()


class BOOK(BaseModel):
    id: UUID
    title: str
    author: str
    description: str
    rating: int


BOOKS = []


@app.get("/")
async def books():
    return BOOKS


@app.post("/")
async def create_book(book: BOOK):
    BOOKS.append(book)
    return book
