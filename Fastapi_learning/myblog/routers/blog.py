from fastapi import APIRouter, Depends, status ,HTTPException
from typing import List
from .. import schemas, database, models
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)  # Instantiate the APIRouter class with parentheses
get_db = database.get_db


# Create a new blog entry
@router.post('/',status_code=status.HTTP_201_CREATED)
def create(blog: schemas.Blog, db: Session = Depends(get_db)):
    # Creating a new Blog instance using the provided data
    new_blog = models.Blog(title=blog.title, body=blog.body,user_id =1)  

    db.add(new_blog)  # Add the new_blog instance to the session

    db.commit()  # Commit the session to persist the changes in the database

    db.refresh(new_blog)  # Refresh the new_blog instance to update its properties
    
    return new_blog  # Return the newly created blog entry


# Get blogs from the database
@router.get('/', response_model=List[schemas.showBlog])#it will just response blog as defined in schemass
def allBlogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs



#delete the selected id from db
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} not found")

    db.delete(blog)
    db.commit()
    return 'Successful'


#update the blog in database
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, blog: schemas.Blog, db: Session = Depends(get_db)):
    existing_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not existing_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} not found")

    existing_blog.title = blog.title
    existing_blog.body = blog.body

    db.commit()
    return 'Updated Successfully'



#get blog by id from the database
@router.get('/{id}', status_code=status.HTTP_200_OK,response_model=schemas.showBlog)
def show(id , db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Blog with ID {id} not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with ID {id} is not available")
    return blog