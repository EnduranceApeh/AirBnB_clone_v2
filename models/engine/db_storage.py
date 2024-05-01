#!/usr/bin/python3
"""
module DBStorage
"""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.user import User

class DBStorage:
    """DBStorage definition"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of attribute"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"
                .format(
                    getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
                pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
         """Query on the current database session."""
         objects = {}
         if cls:
             query = self.__session.query(cls).all()
             for obj in query:
                 key = "{}.{}".format(type(obj).__name__, obj.id)
                 objects[key] = obj
             else:
                 classes = [State, City, User, Amenity, Place, Review]
                 for cls in classes:
                     query = self.__session.query(cls).all()
                     for obj in query:
                         key = "{}.{}".format(type(obj).__name__, obj.id)
                         objects[key] = obj
                         return objects

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Database and value creation and configuration"""
        # create session from current engine
        Base.metadata.create_all(self.__engine)

        # create database table
        ses_scope = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses_scope)
        self.__session = Session()

    def close(self):
        """closes session"""
       self.__session.close()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.close()
