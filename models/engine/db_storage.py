"""
This module instantiates an object of class DBStorage to manage database storage.

The DBStorage class manages the storage of hbnb models in a database. It uses SQLAlchemy to create an engine and session for database operations.
"""
#!/usr/bin/python3
...
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


def __init__(self):
    "initializes the dbstorage engine"
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, scoped_session
    from models.base_model import BaseModel
    import os

    user = os.getenv('HBNB_MYSQL_USER')
    password = os.getenv('HBNB_MYSQL_PWD')
    host = os.getenv('HBNB_MYSQL_HOST', default='localhost')
    database = os.getenv('HBNB_MYSQL_DB', default='hbnb_dev_db')
    dialect = 'mysql'
    driver = 'mysqldb'

    self.__engine = create_engine(f'{dialect}+{driver}://{user}:{password}@{host}/{database}', pool_pre_ping=True)
    if os.getenv('HBNB_ENV') == 'test':
        BaseModel.metadata.drop_all(self.__engine)


def all(self, cls=None):
   """queries all obj depending
     on the class name (argcls)"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

def get_objects(self, cls):
    return {f"{cls.__name__}.{obj.id}": obj for obj in self.__session.query(cls)}

def get_all_objects(self, cls):
    self.classes = cls
    classes = [BaseModel, User, State, City, Place, Amenity, Review]

    if cls:
        return self.get_objects(cls)
    else:
        return {f"{cls.__name__}.{obj.id}": obj for cls in classes for obj in self.__session.query(cls)}


def new(self, obj):
    """add the object to the current database session"""
    self.__session.add(obj)

def save(self):
    """commit all changes of the current database session"""
    self.__session.commit()

def delete(self, obj=None):
    """delete from the current database session obj if not None"""
    if obj:
        self.__session.delete(obj)

def reload(self):
    """creates all tables in the database (feature of SQLAlchemy)"""
    from models.base_model import BaseModel, Base
    from models.user import User
    from models.state import State
    from models.city import City
    from models.place import Place
    from models.amenity import Amenity
    from models.review import Review
    from sqlalchemy.orm import sessionmaker

    Base.metadata.create_all(self.__engine)
    self.__session = scoped_session(sessionmaker(expire_on_commit=False))
