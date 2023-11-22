#!/usr/bin/python3
"""
Module containing the Amenity class.
"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity

class Amenity(BaseModel, Base):
    """
    The Amenity class represents an amenity in the application.

    Attributes:
        __tablename__ (str): Represents the table name, which is 'amenities'.
        name (str): Represents a column containing a string (128 characters).
                    It can't be null.
        place_amenities (relationship): Represents a Many-To-Many relationship
                                        between Place and Amenity.
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
