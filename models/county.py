#!/usr/bin/python
"""
module containing the County model
"""
from models.base_model import BaseModel

class County(BaseModel):
    """declare class County"""
    name = ''
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)
