#!/usr/bin/python3
"""
module containing the class Registrant
"""
from models .base_model import BaseModel

class Registrant(BaseModel):
    """class Registrant declaration"""
    f_name = ''
    l_name = ''
    profile = ''
    age = 0
    email = ''
    county = ''
    subcounty = ''
    location = ''
    
    def __init__(self, *args, **kwargs):
        """init class Registrant"""
        super().__init__(*args, **kwargs)