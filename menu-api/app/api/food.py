# app/api/food.py

from fastapi import APIRouter
from app.models.schemas import Food, Category, Hotel

router = APIRouter()

hotels = [
    Hotel(id=2, name="Hotel America", slug="America"),
    Hotel(id=4, name="Hotel Plaza", slug="plaza"),
    Hotel(id=5, name="Hotel Riviera", slug="riviera"),
    Hotel(id=1, name="Hotel Luton", slug="luton"),
    Hotel(id=3, name="Hotel Arnold", slug="Arnold"),
]

foods = [
    Food(
        id=1,
        name="Spicy Chicken Wings",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=1,
        hotels_list=hotels[:3],
        metacritic=92,
    ),
    Food(
        id=2,
        name="Tangy Tomato Basil Soup",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=2,
        hotels_list=hotels[:2],
        metacritic=76,
    ),
    Food(
        id=3,
        name="Cheesy Mozzarella Sticks",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=1,
        hotels_list=hotels[:4],
        metacritic=40,
    ),
    Food(
        id=4,
        name="Grilled Steak with Mashed Potatoes",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=3,
        hotels_list=hotels[:2],
        metacritic=73,
    ),
    Food(
        id=5,
        name="Grilled Chicken Caesar Salad",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=2,
        hotels_list=hotels[:3],
        metacritic=52,
    ),
    Food(
        id=6,
        name="Grilled Chicken Caesar Salad",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=2,
        hotels_list=hotels[:4],
        metacritic=97,
    ),
    Food(
        id=7,
        name="Classic Cheeseburger",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=4,
        hotels_list=hotels[:4],
        metacritic=35,
    ),
    Food(
        id=8,
        name="Mint Mojito",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=10,
        hotels_list=hotels[:2],
        metacritic=55,
    ),
    Food(
        id=9,
        name="Decadent Chocolate Lava Cake",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=9,
        hotels_list=hotels[:4],
        metacritic=77,
    ),
    Food(
        id=10,
        name="Cauliflower Buffalo Bites",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=7,
        hotels_list=hotels[:3],
        metacritic=29,
    ),
    Food(
        id=11,
        name="Creamy Spinach Artichoke Dip",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=1,
        hotels_list=hotels[:3],
        metacritic=92,
    ),
    Food(
        id=12,
        name="Classic Chicken Noodle Soup",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=2,
        hotels_list=hotels[:2],
        metacritic=76,
    ),
    Food(
        id=13,
        name="Lentil Curry with Basmati Rice",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=7,
        hotels_list=hotels[:4],
        metacritic=40,
    ),
    Food(
        id=14,
        name="Creamed Spinach with Nutmeg",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=8,
        hotels_list=hotels[:2],
        metacritic=73,
    ),
    Food(
        id=15,
        name="Warm Chocolate Chip Cookies",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=9,
        hotels_list=hotels[:3],
        metacritic=52,
    ),
    Food(
        id=16,
        name="Pepperoni Pizza",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=5,
        hotels_list=hotels[:4],
        metacritic=97,
    ),
    Food(
        id=17,
        name="Chicken Alfredo Pasta",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=5,
        hotels_list=hotels[:4],
        metacritic=35,
    ),
    Food(
        id=18,
        name="Mint Mojito",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=10,
        hotels_list=hotels[:2],
        metacritic=55,
    ),
    Food(
        id=19,
        name="BBQ Pulled Pork Sandwich",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=4,
        hotels_list=hotels[:4],
        metacritic=77,
    ),
    Food(
        id=20,
        name="Crispy Fish and Chips",
        background_image="example.com/spicy_chicken_wings.jpg",
        category_id=6,
        hotels_list=hotels[:3],
        metacritic=29,
    ),
]


@router.get("/")
async def get_foods(category_id: int = None):
    filtered_foods = foods
    if category_id:
        filtered_foods = [food for food in foods if food.category_id == category_id]
    return {"count": len(filtered_foods), "results": filtered_foods}
