#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from mysqlalchemy import Column, String, ForeignKey

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")
