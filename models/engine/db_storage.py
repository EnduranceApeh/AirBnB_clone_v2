#!/usr/bin/python3
"""
module DBStorage
"""
from sqlalchemy import create_engine
from os import getenv

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
        from models.base_model import BaseModel

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

    def 

