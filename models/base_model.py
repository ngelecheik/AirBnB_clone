#!/usr/bin/python3
from datetime import datetime
import uuid
from models import storage
"""This module containts the base model"""


class BaseModel:
    """All classes inherit this class"""

    def __init__(self, *args, **kwargs):
        'constructor of the class'
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key in kwargs:
                if key == "__class__":
                    continue
                if key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(
                        kwargs['updated_at']))
                    continue
                if key == 'created_at':
                    setattr(self, key, datetime.fromisoformat(
                        kwargs['created_at']))
                    continue
                setattr(self, key, kwargs[key])

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()  # removed isoformat here some error might come
        storage.save()

    def to_dict(self):
        """returns a dictionary containing
        all keys/values of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        if isinstance(my_dict["created_at"], datetime):
            my_dict['created_at'] = (my_dict['created_at']).isoformat()
        if isinstance(my_dict['updated_at'], datetime):
            my_dict['updated_at'] = (my_dict['updated_at']).isoformat()

        my_dict['__class__'] = self.__class__.__name__
        return my_dict

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
