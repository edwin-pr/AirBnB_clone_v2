import unittest
from models.state import State
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os


class TestState(unittest.TestCase):
    """
    Test case for the State class.
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

    def test_state_creation(self):
        """
        Test the creation of a State instance.
        """
        state_data = {
            'name': 'California',
        }
        state = State(**state_data)

        self.session.add(state)
        self.session.commit()

        self.assertEqual(state.name, 'California')

    def test_state_relationship(self):
        """
        Test the relationship between State and City.
        """
        state_data = {
            'name': 'New York',
        }
        city_data = {
            'name': 'New York City',
        }
        state = State(**state_data)
        city = City(**city_data)

        state.cities.append(city)

        self.session.add_all([state, city])
        self.session.commit()

        """Retrieve the state from the database and
        check if the relationship exists"""
        retrieved_state = self.session.query(State).filter_by(name='New York').first()
        self.assertEqual(len(retrieved_state.cities), 1)
        self.assertEqual(retrieved_state.cities[0].name, 'New York City')

    def test_name(self):
        """
        Test the 'name' attribute of the State class.
        """
        new = State()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
