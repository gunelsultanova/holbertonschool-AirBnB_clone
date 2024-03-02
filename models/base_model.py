#!/usr/bin/python3
"""
Base model defines all common attributes/methods for other classes
"""


import uuid
from datetime import datetime
from models.engine import storage


class BaseModel:
    """
    Base model for other classes
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
            self.id, self.__dict__)

    def save(self):
        """
        save updates the public instance attribute updated_at with the current
        datetime
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        to_dict returns a dictionary containing all keys/values of __dict__ of
        the instance
        """

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
