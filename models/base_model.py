#!/usr/bin/python3
"""This module defines all common attributes/methods"""
import uuid
from models import storage
from datetime import datetime


class BaseModel:
    """Base class of the AirBnB project"""
    def __init__(self, *args, **kwargs):
        """Instantiation method of the class

        Args:
            args (tuple): tuple of arguments passed
            kwargs (dict): keyword arguments passed
        """
        if kwargs:
            del kwargs['__class__']
            string = "%Y-%m-%dT%H:%M:%S.%f"
            self.created_at = datetime.strptime(kwargs['created_at'], string)
            self.updated_at = datetime.strptime(kwargs['updated_at'], string)
            self.id = kwargs['id']
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """The __str__ magic method
        Returns:
                return a string representation
        """
        string = "[" + str(self.__class__.__name__) + "] ("
        string += str(self.id) + ")" + str(self.__dict__)
        return string

    def save(self):
        """Updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values

        Returns:
            return dictionary represenation of the class
        """
        attr_dictionary = self.__dict__.copy()
        attr_dictionary['__class__'] = self.__class__.__name__
        attr_dictionary['created_at'] = self.created_at.isoformat()
        attr_dictionary['updated_at'] = self.updated_at.isoformat()
        return attr_dictionary
