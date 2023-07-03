from fastapi import FastAPI, Depends ,status ,Response , HTTPException
from database import engine, SessionLocal
from sqlalchemy.orm import Session
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
@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(blog: schemas.Blog, db: Session = Depends(get_db)):
    # Creating a new Blog instance using the provided data
    new_blog = models.Blog(title=blog.title, body=blog.body)  

    db.add(new_blog)  # Add the new_blog instance to the session

    db.commit()  # Commit the session to persist the changes in the database

    db.refresh(new_blog)  # Refresh the new_blog instance to update its properties
    
    return new_blog  # Return the newly created blog entry

#get blog from the database
@app.get('/blog')
def allBlogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

#get blog by id from the database
@app.get('/blog/{id}',status_code=status.HTTP_200_OK)
def show(id,response:Response,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id ==id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Blog with ID {id} not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} is not available")
    return blog