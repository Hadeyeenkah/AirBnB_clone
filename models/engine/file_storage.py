#!/usr/bin/pyhton3
"""This is a module that represents the storage mechanism"""
import json


class FileStorage:
    """File storage class that deaks serialization and deserialization"""
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """Method that returns a dictionary

            Returns:
                return dictionary related to the insatnce
        """
        return FileStorage.__objects

    def new(self, obj):
        """Method sets in __objects the obj with key <obj class name>.id

        Args:
            obj (instance): instance of the class created
        """
        if obj:
            keys = f'{obj.__class__.__name__}.{str(obj.id)}'
            FileStorage.__objects[keys] = obj

    def save(self):
        """Serializes __objects to the JSON file
        """
        dictionary = {}
        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as writting:
            json.dump(dictionary, writting)

    def reload(self):
        """deserializes the JSON file to __objects only if the JSON file exists
            otherwise do nothing
        """
        try:
            with open(FileStorage.__file_path, "r") as reading:
                dictionary = reading.read()
            objects_dict = json.loads(dictionary)
            for obj in objects_dict.values():
                from models.base_model import BaseModel
                name_class = obj['__class__']
                self.new(eval(name_class)(**obj))
        except FileNotFoundError:
            pass
