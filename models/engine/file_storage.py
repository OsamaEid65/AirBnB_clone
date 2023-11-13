#!/usr/bin/python3
"""Module contains FileStorage class"""
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User


class FileStorage:
    """ Class that represents storage engine"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with
        key <obj class name>.id"""

        objcname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objcname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        ogdict = FileStorage.__objects
        objdict = {obj: ogdict[obj].to_dict() for obj in ogdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""

        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
