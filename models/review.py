#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """class for customer reviews

    Args:
        BaseModel (BaseModel)
    """

    place_id = ""  # it will be the Place.id
    user_id = ""  # it will be the User.id
    text = ""
