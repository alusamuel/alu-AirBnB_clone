#!/usr/bin/python3
"""Unit tests for the City class"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test suite for the City class"""

    def setUp(self):
        """Create a City instance before each test"""
        self.city = City()

    def test_inheritance(self):
        """Test that City is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))
        self.assertIsInstance(self.city, BaseModel)

    def test_base_attributes(self):
        """Test for attributes inherited from BaseModel"""
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_name_attribute(self):
        """Test the name attribute exists and defaults to empty string"""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.name, "")

    def test_state_id_attribute(self):
        """Test the state_id attribute exists and defaults to empty string"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.state_id, "")


if __name__ == "__main__":
    unittest.main()