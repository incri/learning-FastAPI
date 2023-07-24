from fastapi import APIRouter ,Depends ,status ,HTTPException
# from .. import schemas , database ,models ,JWTtoken
from sqlalchemy.orm import Session
# from .. hashing import Hashing
from hashing import Hashing
import schemas , database ,models ,JWTtoken

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(authentication : schemas.Login ,db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == authentication.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Invalid Email")
    if not Hashing.verify(user.password,authentication.password):
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Invalid Password")
   

    
    access_token = JWTtoken.create_access_token( data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
