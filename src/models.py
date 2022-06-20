import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    username = Column(String(20),nullable=False)
    email = Column(String(250),nullable=False)
    password = Column(String(250),nullable=False)


class Likes(Base):
    __tablename__ = 'Likes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    post_id = Column(Integer, ForeignKey('Posts.id'))
    Users = relationship(Users)

class Posts(Base):
    __tablename__='Posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('Users.id'))
    photo = Column(String(250))
    description = Column(String(250))
    created_at = Column(DateTime)
    update_at = Column(DateTime)

class Comments(Base):
    __tablename__='Comments'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('Users.id'))
    post_id = Column(Integer,ForeignKey('Posts.id'))
    content = Column(String(250))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Followers(Base):
    __tablename__='Followers'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('Users.id'))
    #accepted = Column(Boolean)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e