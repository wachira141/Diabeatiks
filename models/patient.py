#!/usr/bin/python3

"""
module that contains the Patients model
"""
from models.registrant import Registrant

class Patient(Registrant):
    """Patient model declaration"""
    diabetes_stage = ''
    height = 0
    weight = 0
    community = ''
    daetician = ''
    doctor = ''
    prescription = []
    physical_routine = '' #will be a list of physical routines per day of the week
    meal_routine = ''
    facility_id = ''

    def __init__(self, *args, **kwargs):
        """init class Patient"""
        super().__init__(*args, **kwargs)