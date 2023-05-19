#!/usr/bin/python3

"""
module that contains the Patients model
"""
from models.registrant import Registrant
from models.base_model import Base
import models
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

class Patient(Registrant, Base):
    """Patient model declaration"""
    if models.storage_type == 'db_storage':
        __tablename__ = 'patient'
        diabetes_stage = Column(String(40))
        height = Column(Float)
        weight = Column(Float)
        communities = relationship('Community', backref='community')
        daetician = Column(String(60), ForeignKey('daetician.id'))
        doctor = Column(String(60), ForeignKey('doctor.id'))
        prescription = relationship('Prescription', backref='patient')


        # meal_routine = ''
        # facility_id = ''
        # physical_routine = '' #will be a list of physical routines per day of the week
    else:
        diabetes_stage = ''
        height = 0
        weight = 0
        community = '' #community joined
        daetician = ''
        doctor = ''
        prescription = []
        physical_routine = '' #will be a list of physical routines per day of the week
        meal_routine = ''
        facility_id = ''

    def __init__(self, *args, **kwargs):
        """init class Patient"""
        super().__init__(*args, **kwargs)