from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm


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


def verify_password(password, hashed_password):
    return bcrypt_context.verify(password, hashed_password)


def authenticate_user(username: str, password: str, db):
    user = db.query(models.Users).filter(models.Users.username == username).first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user 


@app.post("/user/create")
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


@app.post("/user/auth")
async def login(
    form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(form.username, form.password, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not Found")
    return "User Validated"
