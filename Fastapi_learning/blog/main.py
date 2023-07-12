from fastapi import FastAPI, Depends ,status ,Response , HTTPException 
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from hashing import Hashing
from typing import List
import schemas
import models

app = FastAPI()

# Create database tables if they don't exist
models.Base.metadata.create_all(engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new blog entry
@app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['Blogs'])
def create(blog: schemas.Blog, db: Session = Depends(get_db)):
    # Creating a new Blog instance using the provided data
    new_blog = models.Blog(title=blog.title, body=blog.body)  

    db.add(new_blog)  # Add the new_blog instance to the session

    db.commit()  # Commit the session to persist the changes in the database

    db.refresh(new_blog)  # Refresh the new_blog instance to update its properties
    
    return new_blog  # Return the newly created blog entry


#delete the selected id from db
@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=['Blogs'])
def delete_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} not found")

    db.delete(blog)
    db.commit()
    return 'Successful'


#update the blog in database
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['Blogs'])
def update_blog(id, blog: schemas.Blog, db: Session = Depends(get_db)):
    existing_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not existing_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} not found")

    existing_blog.title = blog.title
    existing_blog.body = blog.body

    db.commit()
    return 'Updated Successfully'


#get blog from the database
@app.get('/blog',response_model=List[schemas.showBlog],tags=['Blogs']) #it will just response blog as defined in schemass
def allBlogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


#get blog by id from the database
@app.get('/blog/{id}', status_code=status.HTTP_200_OK,response_model=schemas.showBlog,tags=['Blogs'])
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Blog with ID {id} not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with ID {id} is not available")
    return blog



#creating the user
@app.post('/users',response_model=schemas.Show_User ,status_code=status.HTTP_201_CREATED,tags=['Users'])
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=user.name, email=user.email, password=Hashing.bcrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#get users from database
@app.get('/users/{id}',response_model=schemas.Show_User,tags=['Users'])
def get_user(id ,db: Session = Depends(get_db)):
    users = db.query(models.User).filter(models.User.id == id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with ID {id} is not available")
    return users