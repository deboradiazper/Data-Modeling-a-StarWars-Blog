import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()



class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class CharactersFav(Base):
    __tablename__ = 'characters fav'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('Character.id'))
    user_id= Column(Integer,  ForeignKey("User.id"))

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class PlanetsFav(Base):
    __tablename__ = 'planets fav'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('Planet.id'))
    user_id= Column(Integer, ForeignKey("User.id"))


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(15), nullable=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')