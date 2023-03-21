#!/usr/bin/python3
"""
contains class User_location declaration
"""
from models.base_model import BaseModel

class UserLocation():
    user_id = ''
    county_id = ''
    subcounty = ''
    location_id = ''
    village_id = ''
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)