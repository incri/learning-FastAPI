from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import models
from passlib.context import CryptContext

app = FastAPI()


class User(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str


bcrypt_context = CryptContext(schemes=["bcrypt"])


def hash_password(password):
    return bcrypt_context.hash(password)


@app.post("/create/user")
async def create_user(user: User):
    model = models.Users()
    model.username = user.username
    model.email = user.email
    model.first_name = user.first_name
    model.last_name = user.last_name
    password_hashed = hash_password(user.password)
    model.hashed_password = password_hashed
    model.is_active = True

    return model
