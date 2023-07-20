from fastapi import HTTPException , status
from sqlalchemy.orm import Session
from ..import models ,schemas


def all_blogs(db : Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(blog: schemas.Blog, db : Session):
    # Creating a new Blog instance using the provided data
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id =1)  

    db.add(new_blog)  # Add the new_blog instance to the session

    db.commit()  # Commit the session to persist the changes in the database

    db.refresh(new_blog)  # Refresh the new_blog instance to update its properties
    
    return new_blog  # Return the newly created blog entry


def delete(id : int ,db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} not found")

    db.delete(blog)
    db.commit()
    return 'Successful'


def update(id : int ,blog : schemas ,db : Session):
    existing_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not existing_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} not found")

    existing_blog.title = blog.title
    existing_blog.body = blog.body

    db.commit()
    return 'Updated Successfully'


def showby_id(id : int , db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Blog with ID {id} not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with ID {id} is not available")
    return blog