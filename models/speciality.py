#!/usr/bin/python3

"""
module containing the Speciality class declaration
"""

from models.base_model import BaseModel

class Speciality(BaseModel):
    """class Speciality Declaration"""
    description = ''
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)