#!/usr/bin/python3


"""
Serializes instances to a JSON file and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel


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
                for key in data:
                    FileStorage.__objects[key] = BaseModel(**data[key])
        except Exception:
            pass
