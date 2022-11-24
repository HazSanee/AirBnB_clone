#!/usr/bin/python3
from datetime import datetime
import uuid


class BaseModel():
    """
    BaseModel class defining all common attributes/methods
    for other classes that would be used on this project
    """
    def __init__(self):
        """
        Initialize instance of BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of BaseModel
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Records the last time instance of Basemodel was updated
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns dictionary representation of BaseModel
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict
