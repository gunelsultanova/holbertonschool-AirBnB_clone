#!/usr/bin/python3


"""
Review class inherits from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class for modeling reviews
    """

    place_id = ""
    user_id = ""
    text = ""
