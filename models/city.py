#!/usr/bin/python3
"""
Module containing the City class.
"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place

class City(BaseModel, Base):
    """
    The City class represents a city in the application.

    Attributes:
        __tablename__ (str): Represents the table name, which is 'cities'.
        name (str): Represents a column containing a string (128 characters).
                     It can't be null.
        state_id (str): Represents a column containing a string (60 characters)
                        and serves as a foreign key to the 'states.id' column.
                        It can't be null.
        places (relationship): Represents a relationship with the Place class.
                               Cascade options: 'all, delete, delete-orphan'.
                               Backref: "cities".
    """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
