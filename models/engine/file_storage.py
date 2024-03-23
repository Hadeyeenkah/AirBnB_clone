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
        dictionary = obj.to_dict()
        if dictionary['__class__'] == 'BaseModel':
            key = f"BaseModel.{dictionary['id']}"
            FileStorage.__objects[key] = dictionary

    def save(self):
        """Serializes __objects to the JSON file
        """
        with open(FileStorage.__file_path, "w") as writting:
            json.dump(FileStorage.__objects, writting)

    def reload(self):
        """deserializes the JSON file to __objects only if the JSON file exists
            otherwise do nothing
        """
        try:
            with open(FileStorage.__file_path, "r") as reading:
                FileStorage.__objects = json.load(reading)
        except:
            pass
