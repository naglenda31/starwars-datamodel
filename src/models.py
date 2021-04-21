import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

favorite_characters = Table('user_characters', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('character_id', Integer, ForeignKey('characters.id'))
)

favorite_planets = Table('user_planets', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('planet_id', Integer, ForeignKey('planets.id'))
)

favorite_vehicles = Table('user_vehicles', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('vehicle_id', Integer, ForeignKey('vehicles.id'))
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(20), nullable=False)
    characters = relationship("Character", secondary=favorite_characters)
    planets = relationship("Planet", secondary=favorite_planets)
    vehicles = relationship("Vehicle", secondary=favorite_vehicles)

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(10))
    mass = Column(String(10))
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(10))
    birth_year = Column(String(10))
    gender = Column(String(10))
    homeworld_id = Column(String(250), ForeignKey("planets.id"))
    homeworld = relationship("Planet", back_populates="characters")
    photo_url = Column(String(250))

class Planet(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    characters = relationship("Character", uselist=False)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    photo_url = Column(String(250))

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    vehicle_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    photo_url = Column(String(250))

    
  





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
