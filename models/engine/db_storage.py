#!/usr/bin/python3

class DBStorage:
    """Database storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Create the engine (self.__engine)"""
  

    def all(self, cls=None):
        """Query on the current database session (self.__session)"""

    def new(self, obj):
        """Add the object to the current database session (self.__session)"""

    def save(self):
        """Commit all changes of the current database session (self.__session)"""

    def delete(self, obj=None):
        """Delete from the current database session"""

    def reload(self):
        """Create all tables in the database (feature of SQLAlchemy)"""
