#!/usr/bin/python3

"""
module containing the location class
"""
from models.base_model import BaseModel

class Location(BaseModel):
    """declare class Location"""
    name = ''
    sub_county = ''
    villages = []
    