#!/usr/bin/python3
"""Test case for review class"""
import unittest
from models.review import Review
from models.place import Place
from models.user import User
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os

class TestReview(unittest.TestCase):
    """
    Test case for the Review class.
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

    def test_review_creation(self):
        """
        Test the creation of a Review instance.
        """
        place_data = {
            'name': 'Cozy Apartment',
        }
        user_data = {
            'name': 'John Doe',
        }
        review_data = {
            'text': 'Great place!',
            'place_id': 'Cozy Apartment',
            'user_id': 'John Doe',
        }
        place = Place(**place_data)
        user = User(**user_data)
        review = Review(**review_data)

        self.session.add_all([place, user, review])
        self.session.commit()

        self.assertEqual(review.text, 'Great place!')
        self.assertEqual(review.place_id, place.id)
        self.assertEqual(review.user_id, user.id)

if __name__ == '__main__':
    unittest.main()

class TestReviewExtended(unittest.TestCase):
    """
    Extended test case for the Review class.
    Inherits from TestReview to ensure basic Review functionality is tested.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.name = 'Review'
        self.value = Review

    def tearDown(self):
        """
        Clean up after the tests.
        """
        try:
            os.remove('file.json')
        except:
            pass

    def test_place_id(self):
        """
        Test the 'place_id' attribute of the Review class.
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """
        Test the 'user_id' attribute of the Review class.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """
        Test the 'text' attribute of the Review class.
        """
        new = self.value()
        self.assertEqual(type(new.text), str)

if __name__ == '__main__':
    unittest.main()

