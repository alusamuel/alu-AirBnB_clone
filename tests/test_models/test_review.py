#!/usr/bin/python3
"""Unit tests for the Review class"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test suite for the Review class"""

    def setUp(self):
        """Create a Review instance before each test"""
        self.review = Review()

    def test_inheritance(self):
        """Test that Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes_exist(self):
        """Test that inherited attributes exist"""
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_place_id_attribute(self):
        """Test that place_id attribute exists and is an empty string"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(self.review.place_id, "")

    def test_user_id_attribute(self):
        """Test that user_id attribute exists and is an empty string"""
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")

    def test_text_attribute(self):
        """Test that text attribute exists and is an empty string"""
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "")


if __name__ == "__main__":
    unittest.main()
