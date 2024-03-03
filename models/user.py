#!/usr/bin/python3


"""
User class inherits from BaseModel
"""

from models.base_model import BaseModel



class User(BaseModel):
    """
    User class is blueprint for users data
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
