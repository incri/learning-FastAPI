from sqlalchemy import Column, Integer, String
from database import Base

#for blog
class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

#for user
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String , unique=True, index=True)
    password = Column(String)