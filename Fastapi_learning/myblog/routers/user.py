from fastapi import APIRouter ,HTTPException ,Depends ,status 
from .. import database ,schemas ,models
from ..hashing import Hashing
from sqlalchemy .orm import Session

router = APIRouter()
get_db = database.get_db


#creating the user
@router.post('/users',response_model=schemas.Show_User ,status_code=status.HTTP_201_CREATED,tags=['Users'])
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=user.name, email=user.email, password=Hashing.bcrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#get users from database
@router.get('/users/{id}',response_model=schemas.Show_User,tags=['Users'])
def get_user(id ,db: Session = Depends(get_db)):
    users = db.query(models.User).filter(models.User.id == id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with ID {id} is not available")
    return users