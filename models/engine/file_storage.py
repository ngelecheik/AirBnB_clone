#!/usr/bin/python3
"""This module hosts a class to serialize and deserialize a class"""
import json


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
        type(
            self).__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        print("saving")
        print(type(self).__objects)
        objects_str = str(type(self).__objects)
        objects_str = f"{objects_str}\n"
        with open(type(self).__file_path, 'a', encoding='utf-8') as f:
            f.write(objects_str)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file                                                                                                doesn’t exist, no exception should be raised)"""
        with open(__file_path, encoding='utf-8') as f:
            type(self).__objects = json.loads(f.readline())
