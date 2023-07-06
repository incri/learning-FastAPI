from pydantic import BaseModel

class Blog(BaseModel):
    title : str
    body : str

class showBlog(Blog):
   class Config:
        # Enable Pydantic's ORM mode
        orm_mode = True  # This allows the model to work  with ORMs