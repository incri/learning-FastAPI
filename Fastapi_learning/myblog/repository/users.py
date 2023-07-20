from fastapi import HTTPException , status
from sqlalchemy.orm import Session
from ..hashing import Hashing
from ..import models ,schemas


def create( user : schemas.User, db : Session):
    new_user = models.User(name=user.name, email=user.email, password=Hashing.bcrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def getby_id(id : int , db : Session):
    users = db.query(models.User).filter(models.User.id == id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with ID {id} is not available")
    return users