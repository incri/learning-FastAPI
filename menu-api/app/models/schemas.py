# app/models/schemas.py

from pydantic import BaseModel
from typing import List


class Hotel(BaseModel):
    id: int
    name: str
    slug: str


class Food(BaseModel):
    id: int
    name: str
    background_image: str
    hotels_list: List[Hotel]
    metacritic: int
