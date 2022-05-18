import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):   
    __tablename__ = 'user' 
    id = Column(Integer, primary_key=True)
    nombre = Column(String(20))
    email = Column(String(30))
    password = Column(String(30))

class Planetas(Base):   
    __tablename__ = 'planetas' 
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30))
    population = Column(Integer)
    gravity = Column(String(30))

class Personajes(Base):    
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30))
    estatura = Column(Integer)
    colorOjos = Column(String(30))

class Favoritos_Pl(Base):
    __tablename__ = 'favoritos_PL'
    idFav = Column(Integer, primary_key= True)  
    id_pj = Column(Integer,ForeignKey('Planetas.id'))
    Planetas = relationship('Planetas')
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Favoritos_Pj(Base):
    __tablename__ = 'favoritos_Pj'
    idFav = Column(Integer, primary_key= True)
    id_pj = Column(Integer,ForeignKey('Personajes.id'))
    Personajes = relationship('Personajes')
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)



"""
class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
"""
def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')