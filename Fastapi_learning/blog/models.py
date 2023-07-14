from sqlalchemy import Column, Engine, Integer, String ,ForeignKey
from database import Base
from sqlalchemy.orm import relationship 

#for blog
class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer,ForeignKey('users.id'))
    # Foreign key referencing the user who created the blog

    
    creator = relationship('User', back_populates='blogs')
     # Relationship to the User who created the blog

#for user
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String , unique=True, index=True)
    password = Column(String)

    blogs = relationship('Blog', back_populates='creator')
    # Relationship to the blogs created by the user