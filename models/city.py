#!/usr/bin/python3
""" City Module for HBNB project
with a class City that inherits from BaseModel
and a class attribute name that represents the city
 name and state_id with  a foreign key to states.id
of the State class with a string (60) """

from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class City():
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
