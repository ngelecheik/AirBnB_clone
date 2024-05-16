#!/usr/bin/python3
from datetime import datetime
import uuid
"""This module containts the base model"""


class BaseModel:
    """All classes inherit this class"""
    def __init__(self):
        'constructor of the class'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing
        all keys/values of __dict__ of the instance"""
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        return my_dict

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}]({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
