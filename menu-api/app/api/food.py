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
        name="Spicy Hot Chicken Wings",
        background_image="https://media.istockphoto.com/id/475705413/photo/barbecue-buffalo-chicken-wings.jpg?s=1024x1024&w=is&k=20&c=QtY3_WfRUUiLTy9n6byLfo1FGcGgfFXauQBA9OsfEMs=",
        category_id=1,
        hotels_list=hotels[:3],
        metacritic=92,
    ),
    Food(
        id=2,
        name="Tangy Tomato Basil Soup",
        background_image="https://media.istockphoto.com/id/485328884/photo/fresh-tomato-gazpacho.jpg?s=1024x1024&w=is&k=20&c=hxv4ciDUVrrcjCjg6E--TNvWmCRmtSGbMEvYTTMKDBI=",
        category_id=2,
        hotels_list=hotels[:2],
        metacritic=76,
    ),
    Food(
        id=3,
        name="Cheesy Mozzarella Sticks",
        background_image="https://media.istockphoto.com/id/667107068/photo/breaded-mozzarella-sticks.jpg?s=1024x1024&w=is&k=20&c=TJGvWXhegbjuJVv8IuoO56vlKkN0pxOS4HSed9rkDbE=",
        category_id=1,
        hotels_list=hotels[:4],
        metacritic=40,
    ),
    Food(
        id=4,
        name="Grilled Steak with Mashed Potatoes",
        background_image="https://media.istockphoto.com/id/146768311/photo/a-steak-dinner-with-mashed-potatoes-and-vegetable-medley.jpg?s=1024x1024&w=is&k=20&c=EvJo0j4MQBqQtdJoZcDrrLKqILUmguygGvv-Bo1f214=",
        category_id=3,
        hotels_list=hotels[:2],
        metacritic=73,
    ),
    Food(
        id=5,
        name="Grilled Chicken Caesar Salad",
        background_image="https://media.istockphoto.com/id/169986941/photo/chicken-salad.jpg?s=1024x1024&w=is&k=20&c=mWlIitrFz5dq4GQhDtbK82VUBK7YQN39nX_RVeBB7PA=",
        category_id=2,
        hotels_list=hotels[:3],
        metacritic=52,
    ),
    Food(
        id=6,
        name="Chilled Iced Cold Brew Coffee",
        background_image="https://media.istockphoto.com/id/1164184073/photo/almond-milk-cold-brew-coffee-latte-in-glass-jars.jpg?s=1024x1024&w=is&k=20&c=x1Z-ps91FWirKIcR1KPpzQqx9BTPzmDSaeAOU5B9BbQ=",
        category_id=10,
        hotels_list=hotels[:4],
        metacritic=97,
    ),
    Food(
        id=7,
        name="Classic Cheeseburger",
        background_image="https://media.istockphoto.com/id/854565540/photo/close-up-of-home-made-burgers.jpg?s=1024x1024&w=is&k=20&c=Usn8AYiIIjOaLDNUAfFpbnpIFbAB8qrqbbeRXksaaH4=",
        category_id=4,
        hotels_list=hotels[:4],
        metacritic=35,
    ),
    Food(
        id=8,
        name="Mint Mojito",
        background_image="https://media.istockphoto.com/id/1182646668/photo/cucumber-and-lemon-refreshing-drink-with-mint.jpg?s=1024x1024&w=is&k=20&c=VfWbhxeUuBW4X07Fvs338Qjb6PArB6DXZwySOJQR3X8=",
        category_id=10,
        hotels_list=hotels[:2],
        metacritic=55,
    ),
    Food(
        id=9,
        name="Chocolate Lava Cake",
        background_image="https://media.istockphoto.com/id/450715171/photo/homemade-chocolate-lava-cake-dessert.jpg?s=1024x1024&w=is&k=20&c=o-zyh5JBrI66CaLdR3PTxrZq8IJzwwiWna_orEu5tsM=",
        category_id=9,
        hotels_list=hotels[:4],
        metacritic=77,
    ),
    Food(
        id=10,
        name="Cauliflower Buffalo Bites",
        background_image="https://media.istockphoto.com/id/1278429591/photo/vegan-cauliflower-buffalo-wings-on-white-wooden-board.jpg?s=1024x1024&w=is&k=20&c=uYY8kPAfFFoBlqOvuhRXJ1EigK8fxZwRd5NWEYM6iU0=",
        category_id=7,
        hotels_list=hotels[:3],
        metacritic=29,
    ),
    Food(
        id=11,
        name="Creamy Spinach Artichoke Dip",
        background_image="https://media.istockphoto.com/id/163736441/photo/fresh-organic-artichoke-dip.jpg?s=1024x1024&w=is&k=20&c=eCQGAZVTOpZcvxrzhE6Dc7FXBa-MYrbH7x0IZVxF1n0=",
        category_id=1,
        hotels_list=hotels[:3],
        metacritic=92,
    ),
    Food(
        id=12,
        name="Classic Chicken Noodle Soup",
        background_image="https://media.istockphoto.com/id/489011742/photo/chicken-noodle-soup.jpg?s=1024x1024&w=is&k=20&c=cNtByRjxfI5CAtiDcnyhL8VHTco_4nhORabv-jEiP8E=",
        category_id=2,
        hotels_list=hotels[:2],
        metacritic=76,
    ),
    Food(
        id=13,
        name="Lentil Curry with Basmati Rice",
        background_image="https://media.istockphoto.com/id/1363634479/photo/vegan-red-lentils-curry-with-basmati-rice-all-plant-based-recipe.jpg?s=1024x1024&w=is&k=20&c=nwc263j8euYObsa_vsKhPD4qD5jbLvECMmsQqMLsYc8=",
        category_id=7,
        hotels_list=hotels[:4],
        metacritic=40,
    ),
    Food(
        id=14,
        name="Creamed Spinach with Nutmeg",
        background_image="https://media.istockphoto.com/id/1307610926/photo/traditional-eggs-benedict-florentine-with-poached-eggs-creamed-spinach-green-onions.jpg?s=1024x1024&w=is&k=20&c=hhnJsAafzAeVXMAgNeS40Up2eA96maQl8Rp4_0lxN5A=",
        category_id=8,
        hotels_list=hotels[:2],
        metacritic=73,
    ),
    Food(
        id=15,
        name="Warm Chocolate Chip Cookies",
        background_image="https://media.istockphoto.com/id/93204335/photo/a-dozen-cookies-baking-in-the-oven.jpg?s=1024x1024&w=is&k=20&c=dO_dB7uhMHX2OAbthNAh8KVcjOEXPYuFEvqGzIHSvlE=",
        category_id=9,
        hotels_list=hotels[:3],
        metacritic=52,
    ),
    Food(
        id=16,
        name="Pepperoni Pizza",
        background_image="https://media.istockphoto.com/id/521403691/photo/hot-homemade-pepperoni-pizza.jpg?s=1024x1024&w=is&k=20&c=KnhIQkTXRomTqloOutmCKQO18a8vms_Hn60SqGpOvTY=",
        category_id=5,
        hotels_list=hotels[:4],
        metacritic=97,
    ),
    Food(
        id=17,
        name="Chicken Alfredo Pasta",
        background_image="https://media.istockphoto.com/id/506916161/photo/homemade-fettucini-aflredo-pasta.jpg?s=1024x1024&w=is&k=20&c=KvQQgiHKR8yyMzkoW2amD3RmBc0UBeyaPUd5XiuEefc=",
        category_id=5,
        hotels_list=hotels[:4],
        metacritic=35,
    ),
    Food(
        id=18,
        name="Mango Lassi",
        background_image="https://media.istockphoto.com/id/1365859011/photo/drink-mango-lassi-in-two-glasses-on-rustic-concrete-table-with-fresh-ripe-cut-manfo-from-above.jpg?s=1024x1024&w=is&k=20&c=IQAS-55ya4GWYpS8PirEFR0KdfPmYXK4hXJrVD-TxWk=",
        category_id=10,
        hotels_list=hotels[:5],
        metacritic=98,
    ),
    Food(
        id=19,
        name="BBQ Pulled Pork Sandwich",
        background_image="https://media.istockphoto.com/id/470966981/photo/barbeque-pulled-pork-sandwich-and-fries-on-wooden-board.jpg?s=1024x1024&w=is&k=20&c=_BUWqVlx3h4zd0iHhUXlA8FvyxHnvuzIqSirDeffZs4=",
        category_id=4,
        hotels_list=hotels[:4],
        metacritic=77,
    ),
    Food(
        id=20,
        name="Crunchy Crispy Fish and Chips",
        background_image="https://media.istockphoto.com/id/459488805/photo/fish-and-chips-in-tray.jpg?s=1024x1024&w=is&k=20&c=yIJB6X9_kb6J8TE7TZCdgzLPKHiWYkUdt7pzDwGBRYg=",
        category_id=6,
        hotels_list=hotels[:3],
        metacritic=29,
    ),
]


@router.get("/")
async def get_foods(categories: int = None):
    if categories is None:
        return {"count": len(foods), "results": foods}
    else:
        filtered_foods = [food for food in foods if food.category_id == categories]
        return {"count": len(filtered_foods), "results": filtered_foods}
