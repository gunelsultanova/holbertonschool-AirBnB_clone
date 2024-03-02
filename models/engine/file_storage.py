#!/usr/bin/python3


"""
Serializes instances to a JSON file and deserializes JSON file to instances
"""

import json


class FileStorage:
	__file_path = "file.json"
	__objects = {}

def all(self):
      return self.__objects

def new(self, obj):
      key = "{}.{}".format(type(obj).__name__, obj.id)
      self.__objects[key] = obj

def save(self):
      with open(self.__file_path, mode="w", encoding="utf-8") as file:
      json.dump(self.__objects, file)

def reload(self):
    try:
         with open(self.__file_path, 'r') as file:
             self.__objects = json.load(file)
    except Exception:
        return
