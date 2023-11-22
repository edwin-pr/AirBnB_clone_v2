#!/usr/bin/python3
"""Test case for the Place class"""
import unittest
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os

class TestPlace(unittest.TestCase):
    """
    Test case for the Place class.
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

    def test_place_creation(self):
        """
        Test the creation of a Place instance.
        """
        city_data = {
            'name': 'New York',
        }
        user_data = {
            'name': 'John Doe',
        }
        place_data = {
            'name': 'Cozy Apartment',
            'city_id': 'New York',
            'user_id': 'John Doe',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 100,
        }
        city = City(**city_data)
        user = User(**user_data)
        place = Place(**place_data)

        self.session.add_all([city, user, place])
        self.session.commit()

        self.assertEqual(place.name, 'Cozy Apartment')
        self.assertEqual(place.city_id, city.id)
        self.assertEqual(place.user_id, user.id)
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)

    def test_place_relationship(self):
        """
        Test the relationship between Place, Amenity, and Review.
        """
        city_data = {
            'name': 'San Francisco',
        }
        user_data = {
            'name': 'Jane Doe',
        }
        place_data = {
            'name': 'Modern Loft',
            'city_id': 'San Francisco',
            'user_id': 'Jane Doe',
            'number_rooms': 3,
            'number_bathrooms': 2,
            'max_guest': 6,
            'price_by_night': 150,
        }
        amenity_data = {
            'name': 'WiFi',
        }

        city = City(**city_data)
        user = User(**user_data)
        place = Place(**place_data)
        amenity = Amenity(**amenity_data)

        place.amenities.append(amenity)
        review = Review(text="Great place!", place_id=place.id, user_id=user.id)
        self.session.add_all([city, user, place, amenity, review])
        self.session.commit()

        # Retrieve the place from the database and check if the relationship exists
        retrieved_place = self.session.query(Place).filter_by(name='Modern Loft').first()
        self.assertEqual(len(retrieved_place.amenities), 1)
        self.assertEqual(retrieved_place.amenities[0].name, 'WiFi')
        self.assertEqual(len(retrieved_place.reviews), 1)
        self.assertEqual(retrieved_place.reviews[0].text, 'Great place!')

if __name__ == '__main__':
    unittest.main()

class TestPlaceExtended(unittest.TestCase):
    """
    Extended test case for the Place class.
    Inherits from TestCity to ensure basic City functionality is tested.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.name = 'Place'
        self.value = Place

    def tearDown(self):
        """
        Clean up after the tests.
        """
        try:
            os.remove('file.json')
        except:
            pass

    def test_amenities_property(self):
        """
        Test the 'amenities' property of the Place class.
        """
        place = self.value()
        amenity1 = Amenity(name='WiFi')
        amenity2 = Amenity(name='Parking')

        place.amenities.append(amenity1)
        place.amenities.append(amenity2)

        self.assertEqual(len(place.amenities), 2)
        self.assertIn('WiFi', place.amenities)
        self.assertIn('Parking', place.amenities)

    def test_amenities_property_setter(self):
        """
        Test the 'amenities' property setter of the Place class.
        """
        place = self.value()
        amenity1 = Amenity(name='WiFi')
        amenity2 = Amenity(name='Parking')

        place.amenities = [amenity1, amenity2]

        self.assertEqual(len(place.amenities), 2)
        self.assertIn('WiFi', place.amenities)
        self.assertIn('Parking', place.amenities)

if __name__ == '__main__':
    unittest.main()
