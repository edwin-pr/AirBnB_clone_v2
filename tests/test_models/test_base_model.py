#!/usr/bin/python3
"""Test case for the BaseModel class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    """
    Test case for the BaseModel class.
    """

    def test_base_model_creation(self):
        """
        Test the creation of a BaseModel instance.
        """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_base_model_id_generation(self):
        """
        Test the generation of unique IDs for BaseModel instances.
        """
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_base_model_created_updated_at(self):
        """
        Test the creation of 'created_at' and 'updated_at' attributes.
        """
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_base_model_str_representation(self):
        """
        Test the string representation of a BaseModel instance.
        """
        model = BaseModel()
        model_str = str(model)
        self.assertIn("[BaseModel]", model_str)
        self.assertIn("'id':", model_str)
        self.assertIn("'created_at':", model_str)
        self.assertIn("'updated_at':", model_str)

    def test_base_model_to_dict(self):
        """
        Test the conversion of a BaseModel instance to a dictionary.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_base_model_save(self):
        """
        Test the 'save' method of a BaseModel instance.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_base_model_delete(self):
        """
        Test the 'delete' method of a BaseModel instance.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        model.delete()
        self.assertTrue(hasattr(model, '__class__'))
        self.assertFalse(hasattr(model, 'id'))
        self.assertFalse(hasattr(model, 'created_at'))
        self.assertFalse(hasattr(model, 'updated_at'))

    def test_base_model_from_dict(self):
        """
        Test the creation of a BaseModel instance from a dictionary.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(model.to_dict(), new_model.to_dict())

if __name__ == '__main__':
    unittest.main()

class TestBaseModelExtended(unittest.TestCase):
    """
    Test case for the BaseModel class with additional tests.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.name = 'BaseModelExtended'
        self.value = BaseModel

    def tearDown(self):
        """
        Clean up after the tests.
        """
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """
        Test the default instantiation of BaseModel.
        """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """
        Test instantiation of BaseModel with kwargs.
        """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """
        Test instantiation of BaseModel with kwargs containing an integer.
        """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """
        Test the 'save' method of BaseModel.
        """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """
        Test the string representation of BaseModel.
        """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id, i.__dict__))

    def test_todict(self):
        """
        Test the 'to_dict' method of BaseModel.
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """
        Test instantiation of BaseModel with kwargs containing None.
        """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """
        Test instantiation of BaseModel with kwargs containing only one key.
        """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """
        Test the 'id' attribute of BaseModel.
        """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """
        Test the 'created_at' attribute of BaseModel.
        """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime)

    def test_updated_at(self):
        """
        Test the 'updated_at' attribute of BaseModel.
        """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

if __name__ == '__main__':
    unittest.main()
