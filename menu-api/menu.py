from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update with your frontend URL
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


class Food(BaseModel):
    id: int
    name: str
    background_image: str


@app.get("/foods")
async def get_foods():
    foods = [
        Food(
            id=1,
            name="Pizza",
            background_image="https://media.istockphoto.com/id/1349560847/photo/sausage-and-vegetable-pizza-on-dark-background.jpg?s=1024x1024&w=is&k=20&c=jFhiloPJDC_NMMEfaMxhaRiqF_53AAnFfMQyOayVz_Y=",
        ),
        Food(
            id=2,
            name="Sushi",
            background_image="https://cdn.pixabay.com/photo/2018/08/03/08/33/food-3581341_1280.jpg",
        ),
        Food(
            id=3,
            name="Tacos",
            background_image="https://media.istockphoto.com/id/1167430420/photo/tortilla-wraps-sandwiches-with-fresh-vegetables-minced-meat-and-blood-oranges-on-plate.jpg?s=1024x1024&w=is&k=20&c=anuSQIqO8zLoRyeZlD1NSxbZ07KWdXj6NWH9jaeTUNw=",
        ),
        Food(
            id=4,
            name="Pasta",
            background_image="https://cdn.pixabay.com/photo/2016/11/23/18/31/pasta-1854245_1280.jpg",
        ),
        Food(
            id=5,
            name="Burger",
            background_image="https://media.istockphoto.com/id/1400656321/photo/homemade-cheese-smash-burger.jpg?s=1024x1024&w=is&k=20&c=1pq3Pm6KrGhuBybemZ8RthoK3sZmi8FuwV0esGYkEeM=",
        ),
        Food(
            id=6,
            name="Curry",
            background_image="https://cdn.pixabay.com/photo/2016/07/22/05/07/delicious-1534207_1280.jpg",
        ),
        Food(
            id=7,
            name="Ramen",
            background_image="https://cdn.pixabay.com/photo/2021/12/20/02/07/miso-ramen-6882175_1280.jpg",
        ),
        Food(
            id=8,
            name="Steak",
            background_image="https://cdn.pixabay.com/photo/2015/06/30/22/51/steak-826961_1280.jpg",
        ),
        Food(
            id=9,
            name="Dim Sum",
            background_image="https://cdn.pixabay.com/photo/2015/09/05/20/00/dim-sum-924912_1280.jpg",
        ),
        Food(
            id=10,
            name="Paella",
            background_image="https://cdn.pixabay.com/photo/2016/01/29/13/45/paella-1167973_1280.jpg",
        ),
        Food(
            id=11,
            name="Croissant",
            background_image="https://cdn.pixabay.com/photo/2012/02/29/12/17/bread-18987_1280.jpg",
        ),
        Food(
            id=12,
            name="Kimchi",
            background_image="https://cdn.pixabay.com/photo/2014/01/09/10/14/kimchi-fried-rice-241051_1280.jpg",
        ),
        Food(
            id=13,
            name="Goulash",
            background_image="https://cdn.pixabay.com/photo/2019/02/22/23/50/goulash-4014661_1280.jpg",
        ),
        Food(
            id=14,
            name="Pad Thai",
            background_image="https://cdn.pixabay.com/photo/2019/03/04/12/59/pad-thai-4034040_1280.jpg",
        ),
        Food(
            id=15,
            name="Samosa",
            background_image="https://cdn.pixabay.com/photo/2022/10/09/00/18/samosas-7507951_1280.jpg",
        ),
        Food(
            id=16,
            name="Pierogi",
            background_image="https://cdn.pixabay.com/photo/2017/03/10/13/57/cooking-2132874_1280.jpg",
        ),
        Food(
            id=17,
            name="Poutine",
            background_image="https://cdn.pixabay.com/photo/2015/12/20/17/19/eat-1101439_1280.jpg",
        ),
        Food(
            id=18,
            name="Pho",
            background_image="https://cdn.pixabay.com/photo/2023/05/27/12/37/noodle-soup-8021417_1280.png",
        ),
        Food(
            id=19,
            name="Falafel",
            background_image="https://cdn.pixabay.com/photo/2016/09/06/14/23/authentic-greek-1649223_1280.jpg",
        ),
        Food(
            id=20,
            name="Hamburger",
            background_image="https://cdn.pixabay.com/photo/2019/01/29/18/05/burger-3962996_1280.jpg",
        ),
    ]
    return {"count": len(foods), "results": foods}
