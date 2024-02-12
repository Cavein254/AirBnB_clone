#!/usr/bin/python3


import unittest
from models.base_models import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        #Test if the class initializes
        test_model = BaseModel()
        self.assertIsNotNone(test_model.id)
        self.assertIsNotNone(test_model.created_at)
        self.assertIsNotNone(test_model.updated_at)
    
    def test_save(self):
        #Test if the updated at values change
        test_model = BaseModel()
        initial_updatedat = test_model.updated_at
        test_model.save()
        current_updatedat = test_model.updated_at
        self.assertNotEqual(initial_updatedat, current_updatedat)
    
    def test_to_dict(self):
        #Test if a dictionary is created
        test_model = BaseModel()
        obj_dict = test_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        #Check if all keys match
        keys = ['__class__', 'id', 'created_at', 'updated_at']
        self.assertCountEqual(obj_dict.keys(), keys)
    
    def test_str(self):
        test_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(test_model.id,
                                                    test_model.__dict__)
        self.assertEqual(test_model.__str__(), expected_str)


if __name__ == "__main__":
    unittest.main()
