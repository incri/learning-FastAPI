# app/api/category.py

from fastapi import APIRouter
from app.models.schemas import Category

router = APIRouter()

categories = [
    Category(id=1, name="Appetizers"),
    Category(id=2, name="Soups and Salads"),
    Category(id=3, name="Main Courses"),
    Category(id=4, name="Sandwiches and Burgers"),
    Category(id=5, name="Pizza and Pasta"),
    Category(id=6, name="Seafood Specialties"),
    Category(id=7, name="Vegetarian/Vegan Options"),
    Category(id=8, name="Side Dishes"),
    Category(id=9, name="Desserts"),
    Category(id=10, name="Beverages")
]



@router.get("/")
async def get_categories():
    return {"count": len(categories), "results": categories}


@router.get("/{category_id}")
async def get_category(category_id: int):
    category = next((cat for cat in categories if cat.id == category_id), None)
    if category:
        return category
    else:
        return {"message": "Category not found"}
