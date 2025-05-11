#!/usr/bin/python3
"""Unit tests for the User class"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test suite for the User class"""

    def setUp(self):
        """Create a User instance before each test"""
        self.user = User()

    def test_inheritance(self):
        """Test that User is a subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes_exist(self):
        """Test essential BaseModel attributes exist in User"""
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_user_attributes(self):
        """Test default User attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "")

        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")

        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")

        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")


if __name__ == "__main__":
    unittest.main()
