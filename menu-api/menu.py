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


@app.get("/foods")
async def get_foods():
    foods = [
        Food(id=1, name="Pizza"),
        Food(id=2, name="Sushi"),
        Food(id=3, name="Tacos"),
        Food(id=4, name="Pasta"),
        Food(id=5, name="Burger"),
        Food(id=6, name="Curry"),
        Food(id=7, name="Ramen"),
        Food(id=8, name="Steak"),
        Food(id=9, name="Dim Sum"),
        Food(id=10, name="Paella"),
        Food(id=11, name="Croissant"),
        Food(id=12, name="Kimchi"),
        Food(id=13, name="Goulash"),
        Food(id=14, name="Pad Thai"),
        Food(id=15, name="Samosa"),
        Food(id=16, name="Pierogi"),
        Food(id=17, name="Poutine"),
        Food(id=18, name="Pho"),
        Food(id=19, name="Falafel"),
        Food(id=20, name="Hamburger"),
    ]
    return {"count": len(foods), "results": foods}
