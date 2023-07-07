from fastapi import APIRouter
from app.models.schemas import Size

router = APIRouter()

sizes = [
    Size(id=2, name="S", slug="small"),
    Size(id=4, name="L", slug="large"),
    Size(id=5, name="M", slug="medium"),
    Size(id=1, name="XL", slug="extra_large"),
    Size(id=3, name="XXL", slug="double_extra_large"),
]


@router.get("/")
async def get_sizes():
    return {"count": len(sizes), "results": sizes}
