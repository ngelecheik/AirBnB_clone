#!/usr/bin/python3
import unittest
from models.user import User
'This module is for testing User'


class TestReview(unittest.TestCase):
    """Tests for class User"""

    def test_attributes(self):
        'tests the attibutes of User to be the right data type'
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)
