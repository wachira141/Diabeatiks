#!/usr/bin/python3
"""
contains parent Class BaseModel
inherited b other children 
"""

from datetime import datetime
from uuid import uuid4
import models

time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """Basemodel declaration"""
    def __init__(self, *args, **kwargs):
        """initialize the BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            if kwargs.get('created_at', None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get('updated_at', None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get('id', None) is None:
                self.id = str(uuid4())
        else:

            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
    
    def __str__(self):
        """string representation of our object"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """ persist/save our obj in a fs/db"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()
    def to_dict(self):
        """return a dictionary containing all the key values of the obj"""
        new_dict = {}
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        if new_dict['created_at']:
            new_dict['created_at'] = new_dict['created_at'].strftime(time)
       
        if new_dict['updated_at']:
            new_dict['updated_at'] = new_dict['updated_at'].strftime(time)
       
        return new_dict

    def delete(self):
        """delte the current instance from storage"""
        models.storage.delete(self)
        
