#!/usr/bin/python3
"""
contains Community model
"""
from models.base_model import BaseModel

class Community(BaseModel):
    created_by = ''
    members = ''
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)