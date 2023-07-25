from typing import Optional
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

    class config:
        schema_extra = {
            "example": {
                "id": "UUID",
                "title": "Title OF Book",
                "author": " Author's Name",
                "description": " Description Of Book",
            }
        }


BOOKS = []


@app.get("/")
async def books():
    return BOOKS


@app.post("/")
async def create_book(book: BOOK):
    BOOKS.append(book)
    return book
