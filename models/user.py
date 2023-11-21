#!/usr/bin/python3
"""
Module containing the User class.
"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review

class User(BaseModel, Base):
    """
    The User class represents a user in the application.

    Attributes:
        __tablename__ (str): Represents the table name, which is 'users'.
        email (str): Represents a column containing a string (128 characters).
                     It can't be null.
        password (str): Represents a column containing a string (128 characters).
                        It can't be null.
        first_name (str): Represents a column containing a string (128 characters).
                          It can be null.
        last_name (str): Represents a column containing a string (128 characters).
                         It can be null.
        places (relationship): Relationship with the Place model.
                               Cascade options: 'all, delete, delete-orphan'.
                               Backref: "user".
        reviews (relationship): Relationship with the Review model.
                                Cascade options: 'all, delete, delete-orphan'.
                                Backref: "user".
    """

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
