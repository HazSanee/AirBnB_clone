#!/usr/bin/python3
"""Module containing User class definition"""
from models.base_model import BaseModel


class User(BaseModel):
        """User class definition"""

        email = ""
        password = ""
        first_name = ""
        last_name = ""

        # def __init__(self, *args, **kwargs):
        #     """Initializes instance of User class"""
        #     super().__init__(*args, **kwargs)
        #     storage.new(self)

        # def to_dict(self):
        #     """
        #     Returns dictionary representation of BaseModel
        #     """
        #     inst_dict = self.__dict__.copy()
        #     inst_dict["__class__"] = self.__class__.__name__
        #     inst_dict["created_at"] = self.created_at.isoformat()
        #     inst_dict["updated_at"] = self.updated_at.isoformat()
        #     # print("inst_dict:", inst_dict)
        #     return inst_dict
