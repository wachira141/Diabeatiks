#!/usr/bin/python3
"""
class appoinments that will instatiate appointments objects
"""
from models.base_model import BaseModel
from datetime import datetime

class Appointments(BaseModel):
    """Appointments class declaration"""
    age = 0
    f_name = ''
    l_name = ''
    id_no = 0
    user = '' #fk
    appointer_id = ''
    location = ''
    category = ''
    physical_activities = '' #fk
    prescription = '' #fk
    meal_plan = ''
    file_uploads = '' #fk
    other_med_condt = ''
    appointment_date = ''
    approved = False
    description = ''
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)
