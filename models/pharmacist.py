#!/usr/bin/python3
"""
module containing the Pharmacist class
"""
from models.registrant import Registrant

class Pharmacist(Registrant):
    description = ''
    community = ''
    appointments = False
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)