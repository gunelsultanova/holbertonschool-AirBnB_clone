#!/usr/bin/python3


"""
City class inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for modeling cities
    """

    state_id = ""
    name = ""
