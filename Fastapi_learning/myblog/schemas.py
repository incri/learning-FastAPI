from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title : str
    body : str
   

class Blog(BlogBase):
     class Config:
        orm_mode = True


class User(BaseModel):
    name : str
    email : str
    password : str


class Show_User(BaseModel):
    name : str
    email : str
    blogs : list[Blog] =[]
    class Config:
        orm_mode = True


class showBlog(BaseModel):
    title : str
    body : str
    creator : Show_User
    class Config:
        # Enable Pydantic's ORM mode
        orm_mode = True  # This allows the model to work  with ORMs