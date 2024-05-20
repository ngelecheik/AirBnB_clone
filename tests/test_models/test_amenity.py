#!/usr/bin/python3
import unittest
from models.amenity import Amenity
'This module is for testing Amenity'


class TestAmenity(unittest.TestCase):
    """Tests for class Amenity"""

    def test_attributes(self):
        'tests the attibutes of Amenity to be the right data type'
        self.assertIsInstance(Amenity.name, str)
