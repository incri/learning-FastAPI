from pydantic import BaseModel

class Blog(BaseModel):
    title : str
    body : str

class showBlog(Blog):
   class Config:
        # Enable Pydantic's ORM mode
        orm_mode = True  # This allows the model to work  with ORMs

class User(BaseModel):
    name : str
    email : str
    password : str

class Show_User(BaseModel):
    name : str
    email : str
    class Config:
        orm_mode = True