#!/usr/bin/python3
""" State Module for HBNB project
with a class State that inherits from BaseModel
and a class attribute name that represents the
 state name with a string (128)"""
from sqlalchemy import Column, String
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
