import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    subdate = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'Characters'
    
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    Name = Column(String(250), nullable=False)
    Appearances = Column(String(250))
    Affiliations = Column(String(250))
    Location = Column(String(250))
    Gender = Column(String(250))
    Species = Column(String(250))
    user = relationship(User)

class Locations(Base):
    __tablename__ = 'Locations'
    
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    Name = Column(String(250), ForeignKey('Characters.Location'))
    Planet = Column(String(250))
    Terrain = Column(String(250))
    Species = Column(String(250))
    Resource = Column(String(250))
    Affiliations = Column(String(250))
    user = relationship(User)

class Movies(Base):
    __tablename__ = 'Movies'
    
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    Name = Column(String(250), ForeignKey('Characters.Appearances'))
    Runtime = Column(String(250))
    Rating = Column(String(250))
    ReleaseDate = Column(String(250))
    Genre = Column(String(250))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
