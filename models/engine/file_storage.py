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

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.loads(file.read())
                for key, val in data.items():
                    class_name = key.split('.')[0]
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**val)
                    elif class_name == "Place":
                        self.__objects[key] = Place(**val)
                    elif class_name == "State":
                        self.__objects[key] = State(**val)
                    elif class_name == "City":
                        self.__objects[key] = City(**val)
                    elif class_name == "Amenity":
                        self.__objects[key] = Amenity(**val)
                    elif class_name == "Review":
                        self.__objects[key] = Review(**val)
        except FileNotFoundError:
            pass
