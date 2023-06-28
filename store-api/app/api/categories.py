# app/api/category.py

from fastapi import APIRouter
from app.models.schemas import Category

router = APIRouter()

categories = [
    Category(
        id=1,
        name="T-shirts",
        background_image="https://media.istockphoto.com/id/1450998087/photo/african-american-man-in-white-t-shirt-against-white-background.jpg?s=1024x1024&w=is&k=20&c=C539s71_IVQYxVUKe2CAnGHJq3IO3TFRDVH0tPwCYjg=",
    ),
    Category(
        id=2,
        name="Jeans",
        background_image="https://media.istockphoto.com/id/1392352768/photo/cropped-shot-of-young-slender-woman-in-fashionable-blue-jeans-with-a-high-fit-on-a-white.jpg?s=1024x1024&w=is&k=20&c=uxiU9yIVrBqt5Qa-0uHcYY8g1BHo1EIfvZ2F9NIiBNE=",
    ),
    Category(
        id=3,
        name="Dresses",
        background_image="https://media.istockphoto.com/id/1393067614/photo/fashion-model-in-red-long-waving-luxury-dress-dark-skinned-beauty-woman-with-afro-black.jpg?s=1024x1024&w=is&k=20&c=cdj0IaN4Efc7f7CUqtu1w2qH4NxbNpgxsWqcdNrnw34=",
    ),
    Category(
        id=4,
        name="Hoodies",
        background_image="https://media.istockphoto.com/id/1366972069/photo/portrait-of-cheerful-man-in-orange-hoodie.jpg?s=1024x1024&w=is&k=20&c=T4HiDeNFoIpYgOEuMo8kRlhL-xY0tP6LgjvGMTg0iBc=",
    ),
    Category(
        id=5,
        name="Jackets",
        background_image="https://media.istockphoto.com/id/1342093309/photo/an-urban-young-woman-in-yellow-jacket-against-blue-sky-1.jpg?s=1024x1024&w=is&k=20&c=MBIPYr8yGomajUwy4rIoafyJ5cMQYf_BVCS-INUH52Q=",
    ),
    Category(
        id=6,
        name="Leggings",
        background_image="https://media.istockphoto.com/id/1365012938/photo/fitness-model-in-leggings-with-beautiful-buttocks-sporty-booty.jpg?s=1024x1024&w=is&k=20&c=FbNRdryan5jYe_oqxJqSlb42TLcGMa4xfXFQBBrlteQ=",
    ),
    Category(
        id=7,
        name="Button-down shirts",
        background_image="https://media.istockphoto.com/id/1431057864/photo/modern-business-man-in-casual-blue-shirt-standing-with-crossed-arms-on-blue-background.jpg?s=1024x1024&w=is&k=20&c=1ztNg_LSiHmSkwnV_VtMSOjkKByQzvWZ06XaSiQ9WJc=",
    ),
    Category(
        id=8,
        name="Skirts",
        background_image="https://media.istockphoto.com/id/1063677494/photo/young-pretty-fashioned-girl.jpg?s=1024x1024&w=is&k=20&c=JfzhFmrxQQODgBk1EUi5enL9sKLGyrnc0Lg8B1Y1AZM=",
    ),
    Category(
        id=9,
        name="Shorts",
        background_image="https://media.istockphoto.com/id/1144375229/photo/young-woman-wearing-jeans-shorts.jpg?s=1024x1024&w=is&k=20&c=d5QA1E-c_9vW53Vdok4ee7qbcroi1TbNg_QyfkhuEdw=",
    ),
    Category(
        id=10,
        name="Sweaters",
        background_image="https://media.istockphoto.com/id/1350833930/photo/beautiful-woman-drinking-tea-in-nature.jpg?s=1024x1024&w=is&k=20&c=_PidtaqVnNLEhM5bRO70MLXxh3EV-ysy8Ow6Hh6isXo=",
    ),
]


@router.get("/")
async def get_categories():
    return {"count": len(categories), "results": categories}
