#!/usr/bin/python3
"""
contains Daetician class model
"""
from models.registrant import Registrant

class Daetician(Registrant):
    """ class Daetician"""
    community = ''
    facility_id = ''
    appointments = ''
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)