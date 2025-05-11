#!/usr/bin/python3
"""FileStorage engine – handles serialization and deserialization of models"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Mapping of class names to actual class objects
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}


class FileStorage:
    """Handles saving and loading model instances to/from a JSON file"""

    __file_path = "file.json"  # Path to the JSON file
    __objects = {}             # Stores all instantiated objects

    def all(self):
        """Returns the dictionary of all stored objects"""
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to __objects with key <class name>.id
        """
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to JSON file at __file_path
        """
        json_objects = {
            key: obj.to_dict() for key, obj in self.__objects.items()
        }
        with open(self.__file_path, "w") as file:
            json.dump(json_objects, file)

    def reload(self):
        """
        Deserializes objects from JSON file and loads them into __objects
        """
        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, data in obj_dict.items():
                    cls = classes[data["__class__"]]
                    self.__objects[key] = cls(**data)
        except FileNotFoundError:
            pass  # No file yet – nothing to load

    def delete(self, key):
        """
        Deletes an object from __objects using its key, then saves changes
        """
        if key in self.__objects:
            del self.__objects[key]
            self.save()
