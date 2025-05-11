#!/usr/bin/python3
"""Unit tests for the BaseModel class"""

from models.base_model import BaseModel
import unittest
from unittest import mock
from datetime import datetime
import sys
import os
import models

# Ensure models directory is accessible
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../")))


class TestBaseModel(unittest.TestCase):
    """Test suite for the BaseModel class"""

    def setUp(self):
        """Create a BaseModel instance before each test"""
        self.sample_base = BaseModel()

    def tearDown(self):
        """Cleanup after each test"""
        del self.sample_base

    @mock.patch("models.storage")
    def test_save(self, mock_storage):
        """Test that save() updates 'updated_at' and calls storage methods"""
        first_updated = self.sample_base.updated_at
        self.sample_base.save()
        second_updated = self.sample_base.updated_at

        self.assertNotEqual(first_updated, second_updated)

        self.sample_base.save()
        third_updated = self.sample_base.updated_at

        self.assertNotEqual(second_updated, third_updated)

        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)

    def test_to_dict(self):
        """Test the to_dict() method returns the correct dictionary"""
        instance_dict = self.sample_base.to_dict()

        self.assertIsInstance(instance_dict, dict)
        self.assertIn("__class__", instance_dict)
        self.assertEqual(instance_dict["__class__"], "BaseModel")

        self.assertIsInstance(instance_dict["created_at"], str)
        self.assertIsInstance(self.sample_base.created_at, datetime)

        self.assertIsInstance(instance_dict["updated_at"], str)
        self.assertIsInstance(self.sample_base.updated_at, datetime)

    def test_str_method(self):
        """Test the __str__ method"""
        result = str(self.sample_base)

        self.assertIsInstance(result, str)
        self.assertIn("BaseModel", result)
        self.assertIn(self.sample_base.id, result)
        self.assertIn(str(self.sample_base.__dict__), result)


if __name__ == "__main__":
    unittest.main()
