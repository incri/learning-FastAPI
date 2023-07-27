import sys

sys.path.append("..")

from typing import Optional
from fastapi import APIRouter
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .auth import get_current_user, get_user_exception

router = APIRouter(
    prefix="/profile", tags=["address"], responses={404: {"description": "Not Found"}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Address(BaseModel):
    address = str
    city = str
    state = str
    country = str
    postalcode = str
