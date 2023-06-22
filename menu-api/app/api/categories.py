# app/api/category.py

from fastapi import APIRouter
from app.models.schemas import Category

router = APIRouter()

categories = [
    Category(
        id=1,
        name="Appetizers",
        background_image="https://media.istockphoto.com/id/1224986732/photo/directly-above-view-of-tapas.jpg?s=1024x1024&w=is&k=20&c=Zdgx04vxqMehQgN8L_3mzNcdsQW7B13IXWJwqK8Vmq0=",
    ),
    Category(
        id=2,
        name="Soups and Salads",
        background_image="https://media.istockphoto.com/id/182497692/photo/soup-and-salad.jpg?s=1024x1024&w=is&k=20&c=IKvooWOWOJVrgHfM4zTLavvMs6I9fH1m4y6p6qah0-A=",
    ),
    Category(
        id=3,
        name="Main Courses",
        background_image="https://media.istockphoto.com/id/462154273/photo/grilled-rack-of-lamb-with-vegetables.jpg?s=1024x1024&w=is&k=20&c=E6KYgOQl2nc_xgOawtU8y6q5MDchJOErtCR1AGo0UOk=",
    ),
    Category(
        id=4,
        name="Sandwiches and Burgers",
        background_image="https://media.istockphoto.com/id/526283108/photo/homemade-vegan-pulled-jackfruit-bbq-sandwich.jpg?s=1024x1024&w=is&k=20&c=RwZgKXsegnEpTsgkKBWHwI8HnJ-JHVwrfxNpgemKPkA=",
    ),
    Category(
        id=5,
        name="Pizza and Pasta",
        background_image="https://media.istockphoto.com/id/1166789297/photo/top-view-pasta-and-pizzas.jpg?s=1024x1024&w=is&k=20&c=YbXKnII2a_jsHhvLZTq-pT0zjmj8468_NSS7t6PL1TM=",
    ),
    Category(
        id=6,
        name="Seafood Specialties",
        background_image="https://media.istockphoto.com/id/528504362/photo/fillet-of-mackerel.jpg?s=1024x1024&w=is&k=20&c=vwComMpP5M8rUVyXT9LvjWPLRinEAweBfs5YFHH03Z8=",
    ),
    Category(
        id=7,
        name="Vegetarian/Vegan Options",
        background_image="https://media.istockphoto.com/id/1149105652/photo/delicious-vegan-burgers-made-from-soya-beams-with-yellow-rice-and-salad.jpg?s=1024x1024&w=is&k=20&c=8hOMJ7ze13lzzPO5hbu3065WtHq_Hz2kJcBMkQX1PQM=",
    ),
    Category(
        id=8,
        name="Side Dishes",
        background_image="https://media.istockphoto.com/id/450055727/photo/homemade-thanksgiving-stuffing-in-a-white-bowl.jpg?s=1024x1024&w=is&k=20&c=tyc4uCkObORlrePVJ4y43FbLclNhQk3QP7rSHaCw57M=",
    ),
    Category(
        id=9,
        name="Desserts",
        background_image="https://media.istockphoto.com/id/515447912/photo/blueberry-cheesecake.jpg?s=1024x1024&w=is&k=20&c=szWbEF4ITTmD-Mpu3tCtqxAf0Siw_ViaNISs3wRMeI8=",
    ),
    Category(
        id=10,
        name="Beverages",
        background_image="https://media.istockphoto.com/id/490361148/photo/still-life-pour-or-whiskey-in-to-glass.jpg?s=1024x1024&w=is&k=20&c=Gk1DHkeuyR3KuEK9IWQc-fzlwKmYXgoMQnOkbklcCwU=",
    ),
]


@router.get("/")
async def get_categories():
    return {"count": len(categories), "results": categories}
