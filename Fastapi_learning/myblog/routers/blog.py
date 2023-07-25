from fastapi import APIRouter, Depends, status ,HTTPException
from typing import List
from sqlalchemy.orm import Session
import database ,models ,schemas , OAuth2
from repository import blogs


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)  # Instantiate the APIRouter class with parentheses
get_db = database.get_db


# Create a new blog entry
@router.post('/',status_code=status.HTTP_201_CREATED)
def create(blog: schemas.Blog, db: Session = Depends(get_db),current_user :
              schemas.User = Depends(OAuth2.get_current_user)):
    return blogs.create(blog,db)
    

# Get blogs from the database
@router.get('/', response_model=List[schemas.showBlog])
#it will just response blog as defined in schemas
def allBlogs(db: Session = Depends(get_db),current_user :
              schemas.User = Depends(OAuth2.get_current_user)):
    return blogs.all_blogs(db)
    

#delete the selected id from db
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db),current_user :
              schemas.User = Depends(OAuth2.get_current_user)):
    return blogs.delete(id ,db)
   

#update the blog in database
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, blog: schemas.Blog, db: Session = Depends(get_db),current_user :
              schemas.User = Depends(OAuth2.get_current_user)):
    return blogs.update(id ,blog , db)
 


#get blog by id from the database
@router.get('/{id}', status_code=status.HTTP_200_OK,response_model=schemas.showBlog)
def show(id , db: Session = Depends(get_db),current_user :
              schemas.User = Depends(OAuth2.get_current_user)):
    return blogs.showby_id(id ,db)