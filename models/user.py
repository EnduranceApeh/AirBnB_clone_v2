#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.ext.declarative imoprt declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String



class User(BaseModel, Base):
    """
    This class defines a user by various attributes
    Attribute:
        email: email address
        password: login password
        firstname: user first name
        last_name: user last naame
    """

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
