# app/api/category.py

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_categories():
    categories = [
        "Italian",
        "Mexican",
        "Chinese",
        "Indian",
    ]
    return {"count": len(categories), "results": categories}
