#!/usr/bin/python3
"""BaseModel for AirBNB clone – defines common attributes/methods"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Defines base methods and attributes for all models"""

    def __init__(self, *args, **kwargs):
        """
        Initializes instance:
        - Creates new UUID and timestamps if no kwargs
        - Else loads data from kwargs
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """Returns string: [ClassName] (id) {attributes}"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates `updated_at` and saves to storage"""
        self.updated_at = datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Returns dict with all attributes + class name,
        with timestamps in ISO format
        """
        instance_dict = self.__dict__.copy()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["__class__"] = self.__class__.__name__
        return instance_dict
