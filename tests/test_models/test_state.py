#!/usr/bin/python3
import unittest
from models.state import State
'This module is for testing'


class TestState(unittest.TestCase):
    """Tests all classes and functionality"""

    def test_state_attribute(self):
        self.assertTrue(hasattr(State, "name"))
        self.assertIsInstance(State.name, str)
        State.name = "kenya"
        self.assertEqual(State.name, "kenya")
