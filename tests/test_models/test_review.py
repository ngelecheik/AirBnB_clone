#!/usr/bin/python3
import unittest
from models.review import Review
'This module is for testing Review'


class TestReview(unittest.TestCase):
    """Tests for class Review"""

    def test_attributes(self):
        'tests the attibutes of Review to be the right data type'
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)
