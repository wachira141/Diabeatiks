#!/usr/bin/python3
""" 
module containing the declaration of class Doctor model
"""

from models.registrant import Registrant
from models.base_model import Base
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
import models


class Doctor(Registrant, Base):
    """declare class Doctor"""
    if models.storage_type == 'db_storage':
        __tablename__ = 'doctor'
        communities = relationship('Community', backref='community')
        speciality = Column(String(160), ForeignKey('speciality.id'), nullable=False)
        title = Column(String(60), nullable=False)
        appointments = relationship('Appointments', backref='appointments')
        appointment_status = Column(Boolean, default=True)
        # facility_id = ''
    else:      
        community = ''
        speciality = [] #should be an array
        title = ''
        appointment_status = True
        facility_id = ''
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)