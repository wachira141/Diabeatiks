#!/usr/bin/python3

"""
module containing the location class
"""
from models.base_model import BaseModel

class Location(BaseModel):
    """declare class Location"""
    name = ''
    subcounty = ''
    # villages = []
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)
    