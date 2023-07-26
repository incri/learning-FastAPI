from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional
import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import SessionLocal, engine


class User(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str


bcrypt_context = CryptContext(schemes=["bcrypt"])

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def hash_password(password):
    return bcrypt_context.hash(password)


@app.post("/create/user")
async def create_user(user: User, db: Session = Depends(get_db)):
    model = models.Users()
    model.username = user.username
    model.email = user.email
    model.first_name = user.first_name
    model.last_name = user.last_name
    password_hashed = hash_password(user.password)
    model.hashed_password = password_hashed
    model.is_active = True

    db.add(model)
    db.commit()

    return {"status": 201, "transaction": "Created Successfully"}
