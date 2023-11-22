#!/usr/bin/python3
<<<<<<< HEAD
""" Place Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", cascade="all, delete",
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 backref="place_amenities",
                                 viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ Returns the list of Review instances with
            place_id equals to the current Place.id """
            reviews = models.storage.all(Review)
            lst = []
            for review in reviews.values():
                if review.place_id == self.id:
                    lst.append(review)
            return lst

        @property
        def amenities(self):
            """Amenities getter"""
            amenities = models.storage.all(Amenity)
            lst = []
            for amenity in amenities.values():
                if amenity.id in self.amenity_ids:
                    lst.append(amenity)
            return lst

        @amenities.setter
        def amenities(self, obj):
            """Amenities setter"""
            if type(obj) == Amenity:
=======
"""
Module containing the Place class.
"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models

# Define a Table for the Many-to-Many relationship between Place and Amenity
place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))

class Place(BaseModel, Base):
    """
    The Place class represents a place in the application.

    Attributes:
        __tablename__ (str): Represents the table name, which is 'places'.
        city_id (str): Represents a column containing a string (60 characters)
                       and serves as a foreign key to the 'cities.id' column.
                       It can't be null.
        user_id (str): Represents a column containing a string (60 characters)
                       and serves as a foreign key to the 'users.id' column.
                       It can't be null.
        name (str): Represents a column containing a string (128 characters).
                    It can't be null.
        description (str): Represents a column containing a string (1024 characters).
        number_rooms (int): Represents a column containing an integer.
                            It can't be null and has a default value of 0.
        number_bathrooms (int): Represents a column containing an integer.
                               It can't be null and has a default value of 0.
        max_guest (int): Represents a column containing an integer.
                         It can't be null and has a default value of 0.
        price_by_night (int): Represents a column containing an integer.
                              It can't be null and has a default value of 0.
        latitude (float): Represents a column containing a float.
        longitude (float): Represents a column containing a float.
        amenity_ids (list): Represents a list to store Amenity IDs.

        If HBNB_TYPE_STORAGE is set to "db":
            reviews (relationship): Represents a relationship with the Review class.
                                    Cascade options: 'all, delete, delete-orphan'.
                                    Backref: "place".
            amenities (relationship): Represents a relationship with the Amenity class.
                                      It is also a secondary relationship to the place_amenity table
                                      with the option viewonly=False and back_populates="place_amenities".
        Else (HBNB_TYPE_STORAGE is not "db"):
            reviews (property): Getter property returning a list of Review instances
                                linked to the current Place.
            amenities (property): Getter property returning a list of Amenity IDs.
            amenities (setter): Setter property handling append method for adding
                                an Amenity ID to the attribute amenity_ids.
    """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """
            Getter property returning a list of Review instances linked to the current Place.
            """
            var = models.storage.all()
            lista = []
            result = []
            for key in var:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    lista.append(var[key])
            for elem in lista:
                if (elem.place_id == self.id):
                    result.append(elem)
            return (result)

        @property
        def amenities(self):
            """
            Getter property returning a list of Amenity IDs.
            """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """
            Setter property handling append method for adding an Amenity ID to the attribute amenity_ids.
            """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
>>>>>>> 98e240d554e99de729c925a7150454fd08fb4b09
                self.amenity_ids.append(obj.id)
