from fastapi import APIRouter ,HTTPException ,Depends ,status 
# from .. import database ,schemas ,models
from sqlalchemy .orm import Session
# from ..repository import users
from repository import users
import database ,schemas ,models

router = APIRouter(
    prefix='/users',
    tags=['Users']
)
get_db = database.get_db


#creating the user
@router.post('/',response_model=schemas.Show_User ,status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return users.create(user , db)


#get users from database
@router.get('/{id}',response_model=schemas.Show_User)
def get_user(id ,db: Session = Depends(get_db)):
    return users.getby_id(id , db)