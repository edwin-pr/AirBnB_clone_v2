#!/usr/bin/python3
"""
Module containing the Review class.
"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Review(BaseModel, Base):
    """
    The Review class represents a review in the application.

    Attributes:
        __tablename__ (str): Represents the table name, which is 'reviews'.
        text (str): Represents a column containing a string (1024 characters).
                    It can't be null.
        place_id (str): Represents a column containing a string (60 characters)
                        and serves as a foreign key to the 'places.id' column.
                        It can't be null.
        user_id (str): Represents a column containing a string (60 characters)
                       and serves as a foreign key to the 'users.id' column.
                       It can't be null.
    """

    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
