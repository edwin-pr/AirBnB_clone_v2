#!/usr/bin/python3
"""
    Test case for the Amenity class.
"""
import unittest
from models.amenity import Amenity
from models.place import Place
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class TestAmenity(unittest.TestCase):
    """
    Test case for the Amenity class.
    """

    def setUp(self):
        """
        Set up the testing environment before each test.
        """
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.session = Session(bind=self.engine)

    def tearDown(self):
        """
        Clean up the testing environment after each test.
        """
        self.session.close_all()
        Base.metadata.drop_all(self.engine)

    def test_amenity_creation(self):
        """
        Test the creation of an Amenity instance.
        """
        amenity_data = {
            'name': 'Swimming Pool'
        }
        amenity = Amenity(**amenity_data)

        self.assertEqual(amenity.name, 'Swimming Pool')

    def test_amenity_relationship(self):
        """
        Test the relationship between Place and Amenity.
        """
        amenity_data = {
            'name': 'WiFi'
        }
        place_data = {
            'name': 'Cozy Cottage'
        }

        amenity = Amenity(**amenity_data)
        place = Place(**place_data)

        place.amenities.append(amenity)
        self.session.add(place)
        self.session.commit()

        """ Retrieve the place from the database and
        check if the relationship exists"""
        retrieved_place = self.session.query(Place).filter_by(name='Cozy Cottage').first()
        self.assertEqual(len(retrieved_place.amenities), 1)
        self.assertEqual(retrieved_place.amenities[0].name, 'WiFi')


if __name__ == '__main__':
    unittest.main()
