#!/usr/bin/python3
"""Module containing Review class definition"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class definition"""

    place_id = ""
    user_id = ""
    text = ""
