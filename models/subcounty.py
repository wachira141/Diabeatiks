#!/usr/bin/python3

"""
module containing the subcounty model
"""

from models.base_model import BaseModel

class Subcounty(BaseModel):
    """class Subcounty declaration"""
    name = ''
    county = ''
    locations = []