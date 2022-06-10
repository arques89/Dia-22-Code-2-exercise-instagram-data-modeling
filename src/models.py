import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String , DateTime
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
    name = Column(String(250), nullable=False)
    Second_name = Column(String(250), nullable=False)
    email = Column(String(250),nullable=False)
    subscription_date = Column(DateTime)
    Password = Column(String(250), nullable=False)
    

class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('Users.id'))
 

class Characters(Base):
    __tablename__='Characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    species = Column(String(250))
    homeworld = Column(String(250), nullable=False)
    favoritesid = Column(Integer, ForeignKey('Favorites.id'))
    planetsid = Column(Integer, ForeignKey('Planets.id'))

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(String(250))
    films = Column(String(250), nullable=False)
    residents = Column(String(250))
    favoritesid = Column(Integer, ForeignKey('Favorites.id'))
    charactersid = Column(Integer, ForeignKey('Characters.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')