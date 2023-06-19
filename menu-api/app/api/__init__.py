# app/api/__init__.py

from fastapi import APIRouter

from app.api.food import router as food_router
from app.api.categories import router as category_router

router = APIRouter()

router.include_router(food_router, prefix="/foods", tags=["foods"])
router.include_router(category_router, prefix="/categories", tags=["categories"])
