#!/usr/bin/python3
"""Module containing BaseModel class
which is the base of all classes in the project"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """The base model of all models in HBnB project"""

    def __init__(self, *args, **kwargs):
        """Initializes BaseModel instance"""

        stringform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.strptime(value, stringform)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def to_dict(self):
        """Returns dictionary representation of instance"""

        dictionary = self.__dict__.copy()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__

        return dictionary

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""

        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """Returns string representation of instance"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
