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
    location = ''
    physical_activities = ''
    meal_plan = ''
    file_uploads = ''
    other_med_condt = ''
    appointment_date = ''
    appointment_approved = ''
