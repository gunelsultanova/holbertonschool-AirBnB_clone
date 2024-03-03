#!/usr/bin/python3


"""
Serializes instances to a JSON file and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    FileStorage serializes instances to a JSON file and deserializes JSON
    file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """

        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.loads(file.read())
                for key, val in data.items():
                    class_name = key.split('.')[0]
                    if class_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**val)
                    elif class_name == "Place":
                        FileStorage.__objects[key] = Place(**val)
                    elif class_name == "State":
                        FileStorage.__objects[key] = State(**val)
                    elif class_name == "City":
                        FileStorage.__objects[key] = City(**val)
                    elif class_name == "Amenity":
                        FileStorage.__objects[key] = Amenity(**val)
                    elif class_name == "Review":
                        FileStorage.__objects[key] = Review(**val)
        except FileNotFoundError:
            pass
