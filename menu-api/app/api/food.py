# app/api/food.py

from fastapi import APIRouter

from app.models.schemas import Food, Hotel

router = APIRouter()


@router.get("/")
async def get_foods(category: str = None):
    foods = [
        Food(
            id=1,
            name="Pizza",
            background_image="https://media.istockphoto.com/id/1349560847/photo/sausage-and-vegetable-pizza-on-dark-background.jpg?s=1024x1024&w=is&k=20&c=jFhiloPJDC_NMMEfaMxhaRiqF_53AAnFfMQyOayVz_Y=",
            hotels_list=[
                Hotel(id=2, name="Hotel America", slug="America"),
                Hotel(id=4, name="Hotel Plaza", slug="plaza"),
                Hotel(id=5, name="Hotel Riviera", slug="riviera"),
                Hotel(id=1, name="Hotel Luton", slug="luton"),
            ],
            metacritic=92,
        ),
    ]

    if category:
        foods = [food for food in foods if category.lower() in food.name.lower()]

    return {"count": len(foods), "results": foods}
