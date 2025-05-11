#!/usr/bin/python3
"""Unit tests for the State class"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test suite for the State class"""

    def setUp(self):
        """Create a State instance before each test"""
        self.state = State()

    def test_inheritance(self):
        """Test that State is a subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes_exist(self):
        """Test essential BaseModel attributes exist in State"""
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_name_attribute(self):
        """Test that name attribute exists and is an empty string"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")


if __name__ == "__main__":
    unittest.main()