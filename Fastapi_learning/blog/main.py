from fastapi import FastAPI, Depends
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
@app.post('/blog')
def create(blog: schemas.Blog, db: Session = Depends(get_db)):
    # Creating a new Blog instance using the provided data
    new_blog = models.Blog(title=blog.title, body=blog.body)  

    db.add(new_blog)  # Add the new_blog instance to the session

    db.commit()  # Commit the session to persist the changes in the database

    db.refresh(new_blog)  # Refresh the new_blog instance to update its properties
    
    return new_blog  # Return the newly created blog entry
