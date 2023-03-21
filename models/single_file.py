#!/usr/bin/python3
"""
module containing the class Single_file
"""

from models.base_model import BaseModel

class Single_file(BaseModel):
    """class Single_file declarration"""
    file_uploaded = ''
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)