from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import models


app = FastAPI()


class User(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str


@app.post("/create/user")
async def create_user(user: User):
    model = models.Users()
    model.username = user.username
    model.email = user.email
    model.first_name = user.first_name
    model.last_name = user.last_name
    model.hashed_password = user.password
    model.is_active = True

    return model
