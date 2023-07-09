# app/api/food.py

from fastapi import APIRouter
from app.models.schemas import Product
from app.api.sizes import sizes

router = APIRouter()


products = [
    Product(
        id=1,
        name="Plain White Crew Neck T-Shirt",
        background_image="https://media.istockphoto.com/id/957773894/photo/white-t-shirt-on-a-wooden-surface.jpg?s=1024x1024&w=is&k=20&c=xKluRafVDuxvEcxzvYycFgVcPifpK3ArEs98GUUo5u8=",
        category_id=1,
        sizes_list=sizes[:3],
        metacritic=92,
    ),
    Product(
        id=2,
        name="Floral Print Sundress",
        background_image="https://media.istockphoto.com/id/1293272579/photo/woman-dancing-in-the-nature-field-on-a-sunny-summer-day.jpg?s=1024x1024&w=is&k=20&c=XQiZdkBJIZ1nXo1Gf60hARZxUMrqrOCnV5UhKLZQj6E=",
        category_id=3,
        sizes_list=sizes[:2],
        metacritic=76,
    ),
    Product(
        id=3,
        name="Leather Biker Jacket",
        background_image="https://media.istockphoto.com/id/1355961219/photo/leather-motorcycle-jackets-in-shop.jpg?s=1024x1024&w=is&k=20&c=PlFNSn_rFmjyvjLwZsGDOp9uWGJ5WcY0QHJHSRU2KNk=",
        category_id=5,
        sizes_list=sizes[:4],
        metacritic=40,
    ),
    Product(
        id=4,
        name="Graphic Print V-Neck T-Shirt",
        background_image="https://media.istockphoto.com/id/1495443584/vector/baseball-sports-jersey-t-shirt-design-flat-sketch-vector-illustration-football-jersey-with.jpg?s=1024x1024&w=is&k=20&c=c464UF1zVCeM3jaY0x4KTjFhanI1c_qocpwLQIQ8IkY=",
        category_id=1,
        sizes_list=sizes[:2],
        metacritic=73,
    ),
    Product(
        id=5,
        name="Zip-up Hoodie with Fleece Lining",
        background_image="https://media.istockphoto.com/id/1291585686/photo/sweatshirt-with-iron-zipper-hoodie-isolated-on-white-background.jpg?s=1024x1024&w=is&k=20&c=-pNnGk5PZ2YkgCu_dEUDzN2LgeS_vEW1kqzJxVCKfxs=",
        category_id=4,
        sizes_list=sizes[:3],
        metacritic=52,
    ),
    Product(
        id=6,
        name="Black High-Waisted Leggings",
        background_image="https://media.istockphoto.com/id/1127698637/photo/strong-young-brunette-sportswoman-stretching-her-leg.jpg?s=1024x1024&w=is&k=20&c=i8Q6FEt1sivbQAtkFLYlQO4JzNJqgzJZH8Te2ftb2Ds=",
        category_id=6,
        sizes_list=sizes[:4],
        metacritic=97,
    ),
    Product(
        id=7,
        name="Mesh Panel Workout Leggings",
        background_image="https://media.istockphoto.com/id/1409458560/photo/blank-black-women-sport-leggings-mockup-dark-background.jpg?s=1024x1024&w=is&k=20&c=-1G6gzWca7EfQ7xfadHCMb8dOpPqMyH3_YRje2unsjo=",
        category_id=6,
        sizes_list=sizes[:4],
        metacritic=35,
    ),
    Product(
        id=8,
        name="Maxi Skirt with Slit",
        background_image="https://media.istockphoto.com/id/1142243697/photo/stylish-blue-checkered-stripy-skirt-isolated-on-white-background-hype-fashion-magazine-photo.jpg?s=1024x1024&w=is&k=20&c=wyU3H-elPql3VxrF2Edy82WMidp8YrUInDqfCiqDJ_E=",
        category_id=8,
        sizes_list=sizes[:2],
        metacritic=55,
    ),
    Product(
        id=9,
        name="Cashmere V-Neck Sweater",
        background_image="https://media.istockphoto.com/id/1453913379/photo/partial-closeup-of-a-flannel-vest.jpg?s=1024x1024&w=is&k=20&c=xV0IQpw6qFPEGbaSJgeyJWJABHh_D3B-mpPbMQB9HrM=",
        category_id=6,
        sizes_list=sizes[:4],
        metacritic=77,
    ),
    Product(
        id=10,
        name="Cardigan Sweater with Buttons",
        background_image="https://media.istockphoto.com/id/1456619910/photo/striped-womens-cardigan.jpg?s=1024x1024&w=is&k=20&c=5axX0tUO4YyEWQXRNGIk1pyjNROhQbZO64axnBOapX8=",
        category_id=10,
        sizes_list=sizes[:3],
        metacritic=29,
    ),
    Product(
        id=11,
        name="Flared Denim Jeans",
        background_image="https://media.istockphoto.com/id/163736441/photo/fresh-organic-artichoke-dip.jpg?s=1024x1024&w=is&k=20&c=eCQGAZVTOpZcvxrzhE6Dc7FXBa-MYrbH7x0IZVxF1n0=",
        category_id=2,
        sizes_list=sizes[:3],
        metacritic=92,
    ),
    Product(
        id=12,
        name="Striped Long Sleeve T-Shirt",
        background_image="https://media.istockphoto.com/id/468744676/photo/close-up-a-womans-legs-posing-in-jeans-in-the-city.jpg?s=1024x1024&w=is&k=20&c=jSUlP_eAmvKIRwxjo2_nCBaSrQ7w-1yUSnyceXDhnwg=",
        category_id=1,
        sizes_list=sizes[:2],
        metacritic=76,
    ),
    Product(
        id=13,
        name="Distressed Boyfriend Jeans",
        background_image="https://media.istockphoto.com/id/186870715/photo/blue-jeans.jpg?s=1024x1024&w=is&k=20&c=8-g8jkDtNOYnC4mnkDVY0DSDpR5hpVPxlKMAAMsGUuM=",
        category_id=2,
        sizes_list=sizes[:4],
        metacritic=40,
    ),
    Product(
        id=14,
        name="Bomber Jacket in Satin Finish",
        background_image="https://media.istockphoto.com/id/1325183814/photo/mens-bomber-jacket-and-shirt-isolated-on-white-background-fashionable-casual-wear.jpg?s=1024x1024&w=is&k=20&c=2ymYk6vQHzIjzo7q2IGg5YAqGyIaFqBEqHagaYy_5cY=",
        category_id=5,
        sizes_list=sizes[:2],
        metacritic=73,
    ),
    Product(
        id=15,
        name="Athletic Shorts with Moisture-Wicking Fabric",
        background_image="https://media.istockphoto.com/id/93204335/photo/a-dozen-cookies-baking-in-the-oven.jpg?s=1024x1024&w=is&k=20&c=dO_dB7uhMHX2OAbthNAh8KVcjOEXPYuFEvqGzIHSvlE=",
        category_id=9,
        sizes_list=sizes[:3],
        metacritic=52,
    ),
    Product(
        id=16,
        name="Cardigan Sweater with Buttons",
        background_image="https://media.istockphoto.com/id/973969690/photo/khaki-trousers-close-up-fashionable-concept.jpg?s=1024x1024&w=is&k=20&c=zgfP9rOWkJBlOBrpqbb31_Hy4cetHXwjd745xXtds4M=",
        category_id=10,
        sizes_list=sizes[:4],
        metacritic=97,
    ),
    Product(
        id=17,
        name="Hoodie Dress",
        background_image="https://media.istockphoto.com/id/660274432/photo/blank-black-and-white-sweatshirt-mockup-hanging-on-wooden-hanger.jpg?s=1024x1024&w=is&k=20&c=n6c-4ERNuaQuSQxxyCXU9GpMMK1DW1f3snq18arAbuo=",
        category_id=4,
        sizes_list=sizes[:4],
        metacritic=35,
    ),
    Product(
        id=18,
        name="A-Line Cocktail Dress",
        background_image="https://media.istockphoto.com/id/1404788250/vector/wedding-dress-and-black-tie.jpg?s=1024x1024&w=is&k=20&c=6-DKid2jL9xkx3ij8cLhYeiXMLMmm6jrCZnZnW4RxzQ=",
        category_id=3,
        sizes_list=sizes[:5],
        metacritic=98,
    ),
    Product(
        id=19,
        name="Henley T-Shirt",
        background_image="https://media.istockphoto.com/id/452783259/photo/mid-adult-man-portrait.jpg?s=1024x1024&w=is&k=20&c=ntuWf-VW9Ap7uspDyJ2BpLytFlm9gkZQf6vVR7bx8M0=",
        category_id=1,
        sizes_list=sizes[:4],
        metacritic=77,
    ),
    Product(
        id=20,
        name="Printed Yoga Leggings",
        background_image="https://media.istockphoto.com/id/1346346979/photo/panoramic-banner-of-athletic-woman-dressed-in-sportswear-performing-stretches-with-a-large.jpg?s=1024x1024&w=is&k=20&c=Qvrz3VTyAkafGstiiX2II60kOWSThY_L9MUCt8jY7bc=",
        category_id=6,
        sizes_list=sizes[:3],
        metacritic=29,
    ),
]


@router.get("/")
async def get_products(
    categories: int = None,
    selected_size: int = None,
    sort_by: str = None,
    search_name: str = None,
):
    if categories is None and selected_size is None:
        filtered_products = products

    else:
        filtered_products = products

        if categories is not None:
            filtered_products = [
                product
                for product in filtered_products
                if product.category_id == categories
            ]

        if selected_size is not None:
            filtered_products = [
                product
                for product in filtered_products
                if any(size.id == selected_size for size in product.sizes_list)
            ]

    if search_name:
        filtered_products = [
            product
            for product in filtered_products
            if search_name.lower() in product.name.lower()
        ]

    if sort_by == "name":
        filtered_products.sort(key=lambda product: product.name)
    elif sort_by == "metacritic":
        filtered_products.sort(key=lambda product: product.metacritic, reverse=True)

    return {"count": len(filtered_products), "results": filtered_products}
