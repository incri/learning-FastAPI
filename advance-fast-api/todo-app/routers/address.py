import sys

sys.path.append("..")

from typing import Optional
from fastapi import APIRouter, Depends
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
    address: str
    city: str
    state: str
    country: str
    postalcode: str


@router.post("/address/")
async def create_address(
    address: Address,
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if user is None:
        raise get_user_exception()

    model = models.Address()
    model.address = address.address
    model.city = address.city
    model.state = address.state
    model.country = address.country
    model.postalcode = address.postalcode

    db.add(model)
    db.flush()

    user_model = (
        db.query(models.Users).filter(models.Users.id == user.get("id")).first()
    )
    user_model.address_id = model.id
    db.add(user_model)
    db.commit()
