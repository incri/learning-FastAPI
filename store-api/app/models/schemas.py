# app/models/schemas.py

from pydantic import BaseModel
from typing import List


class Size(BaseModel):
    id: int
    name: str
    slug: str


class Product(BaseModel):
    id: int
    name: str
    background_image: str
    sizes_list: List[Size]
    metacritic: int
    category_id: int


class Category(BaseModel):
    id: int
    name: str
    background_image: str
