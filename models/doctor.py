#!/usr/bin/python3
""" 
module containing the declaration of class Doctor model
"""

from models.registrant import Registrant

class Doctor(Registrant):
    """declare class Doctor"""
    community = ''
    facility_id = ''
    speciality = ''
    title = ''
    appointments = False
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)