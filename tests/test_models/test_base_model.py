#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

'This module is for testing'


class TestBaseModel(unittest.TestCase):
    """Tests all classes and functionality"""
    def test_save(self):
        'test the save function'
        basemodel = BaseModel()
        intial_time = basemodel.updated_at
        updated_time = basemodel.save()
        self.assertNotEqual(intial_time, updated_time)

    def test_todict(self):
        'test the todict() function'
        basemodel = BaseModel()
        self.assertIn('__class__', basemodel.to_dict())
