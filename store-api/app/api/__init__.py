# app/api/__init__.py

from fastapi import APIRouter

from app.api.product import router as product_router
from app.api.categories import router as category_router
from app.api.sizes import router as size_router

router = APIRouter()

router.include_router(product_router, prefix="/products", tags=["products"])
router.include_router(category_router, prefix="/categories", tags=["categories"])
router.include_router(size_router, prefix="/sizes", tags=["sizes"])
