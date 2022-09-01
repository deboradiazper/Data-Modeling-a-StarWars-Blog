import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    email = Column(String(250), nullable=False)
    Password =Column (Integer)
    
class Planets(Base):
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(120) ) 
    description = Column(String(500))
    url = Column(String(200))
    terrain = Column(String(120))
    climate = Column(String(120))
    population = Column(Integer)
    gravity = Column(Integer)
    diameter = Column(Integer)

class Character(Base):
    __tablename__= 'character'
    id = Column(Integer, primary_key=True)
    Name = Column(String(120))
    Description = Column(String(300))
    Url = Column(String(120))    
    gender = Column(String(50))
    birth_year = Column(Integer)
    height = Column(Integer)
    Planet =Column (String(250), ForeignKey('planets.id')) 


class Favorites(Base):
    __tablename__= 'favorites'
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    Planet_id= Column(Integer, ForeignKey('planets.id'), nullable=True)
    People_id= Column(Integer, ForeignKey('character.id'), nullable=True)
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
