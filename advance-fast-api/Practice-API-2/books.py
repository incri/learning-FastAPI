from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()


class BOOK(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: Optional[str] = Field(title="Name Of Author", max_length=50, min_length=1)
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
