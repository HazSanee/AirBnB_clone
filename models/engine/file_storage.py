#!/usr/bin/python3
"""Module containing file strorage class definition"""
import json
import os


class FileStorage():
    """
    Storage engine class that serializes instances
    to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        obj_dicts = {**self.__objects}
        for key, obj in obj_dicts.items():
            obj_dicts[key] = obj.to_dict()

        buf = json.dumps(obj_dicts)

        with open(self.__file_path, 'w') as fd:
            fd.write(buf)

    def classes(self):
        """
        Returns a dictionary of valid classes and their references
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
                    "BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review
                    }
        return classes

    def reload(self):
        """
        deserializes the JSON file to __objects
        only if the JSON file (__file_path) exists
        """
        if not os.path.exists(self.__file_path):
            return

        with open(self.__file_path, 'r') as fd:
            content = fd.read()
            if content == "":
                return
            else:
                json_dicts = json.loads(content)

        for key, value in json_dicts.items():
            json_dicts[key] = self.classes()[value['__class__']](**value)

        self.__objects = {**json_dicts}
