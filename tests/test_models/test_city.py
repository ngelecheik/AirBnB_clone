#!/usr/bin/python3
import unittest
from models.city import City
'This module is for testing'


class TestCity(unittest.TestCase):
    """Tests all classes and functionality"""

    def test_attributes(self):
        'tests the attibutes of city to be the right data type'
        self.assertIsInstance(City.state_id, str)
        self.assertIsInstance(City.name, str)
