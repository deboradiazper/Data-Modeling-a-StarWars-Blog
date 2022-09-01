# import os
# import sys
# from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine
# from eralchemy import render_er

# Base = declarative_base()



# class Character(Base):
#     __tablename__ = 'characters'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class CharactersFav(Base):
#     __tablename__ = 'characters fav'
#     id = Column(Integer, primary_key=True)
#     character_id = Column(Integer, ForeignKey('Character.id'))
#     user_id= Column(Integer,  ForeignKey("User.id"))

# class Planet(Base):
#     __tablename__ = 'planets'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class PlanetsFav(Base):
#     __tablename__ = 'planets fav'
#     id = Column(Integer, primary_key=True)
#     planet_id = Column(Integer, ForeignKey('Planet.id'))
#     user_id= Column(Integer, ForeignKey("User.id"))


# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     email = Column(String(250), nullable=False)
#     password = Column(String(15), nullable=False)


#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
# render_er(Base, 'diagram.png')

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
    Subscription = Column (String(50), nullable=False)
    
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
    eye_color = Column(String(120))    
    hair_color = Column(String(120))   
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