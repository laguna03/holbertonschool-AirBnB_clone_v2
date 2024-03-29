#!/usr/bin/python3
"""This module instantiates an object of class DBStorage
 to manage data base storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel
from os import getenv

class DBStorage:
    """This class manages storage of hbnb models in a database"""
    __engine = None
    __session = None

