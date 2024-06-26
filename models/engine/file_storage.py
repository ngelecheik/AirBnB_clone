#!/usr/bin/python3
"""This module hosts a class to serialize and deserialize a class"""
import json
import os


class FileStorage:
    """serializes instances to a JSON file and 
    deserializes JSON file to instances:"""
    __file_path = "./file.json"
    __objects = dict()

    def all(self):
        """ returns the dictionary __objects"""
        return type(self).__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        type(self).__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objects_json = json.dumps(type(self).__objects)
        with open(type(self).__file_path, 'w', encoding='utf-8') as f:
            f.write(objects_json)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file                                                                                                doesn’t exist, no exception should be raised)"""
        if os.path.exists(type(self).__file_path):
            with open(type(self).__file_path, encoding='utf-8') as f:
                type(self).__objects = json.loads(f.read())
