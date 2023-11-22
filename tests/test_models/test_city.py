#!/usr/bin/python3
"""Test case for the City class"""
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class TestCity(TestBaseModel):
    """
    Test case for the City class.
    Inherits from TestBaseModel to ensure basic BaseModel
    functionality is tested.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the TestCity test case.
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Test the 'state_id' attribute of the City class.
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Test the 'name' attribute of the City class.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
