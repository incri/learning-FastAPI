from fastapi import APIRouter
from app.models.schemas import Hotel

router = APIRouter()

hotels = [
    Hotel(id=2, name="Grand America", slug="America"),
    Hotel(id=4, name="Elite Plaza", slug="plaza"),
    Hotel(id=5, name="Riviera Palace", slug="riviera"),
    Hotel(id=1, name="Manor Luton", slug="luton"),
    Hotel(id=3, name="The Arnold Regent", slug="Arnold"),
]


@router.get("/")
async def get_hotels():
    return {"count": len(hotels), "results": hotels}
