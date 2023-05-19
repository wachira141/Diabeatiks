#!/usr/bin/python3
"""
class appoinments that will instatiate appointments objects
"""
from models.base_model import BaseModel, Base
from models import storage_type
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship


class Appointments(BaseModel, Base):
    """Appointments class declaration"""

    if storage_type == 'db_storage':
        __tablename__ = 'appointments'
        age = Column(Integer, nullable=False)
        f_name = Column(String(20), nullable=False)
        l_name = Column(String(20), nullable=False)
        id_no = Column(String(20), nullable=True)
        # user = ForeignKey()
        # appointer_id = ForeignKey()  #enum value
        location = Column(String(50), ForeignKey('location.id'))
        category = Column(String(50), nullable=False, default='general')
        prescription = relationship('prescription', backref='appointments')
        file_uploads = Column(String(50), ForeignKey('files.id'), nullable=False)
        other_med_condt = Column(String(140), nullable=True)
        appointment_date = Column(DateTime, default=datetime.utcnow) #default should be 1 month ahead
        approved = Column(Boolean, default=False)
        description = Column(String(1024), nullable=True)

        # physical_activities = Column(String(60), ForeignKey('physical.id'))
        # meal_plan = Column(String(60), ForeignKey('meal.id'))
    else:
        age = 0
        f_name = ''
        l_name = ''
        id_no = 0
        user = '' #fk
        appointer_id = ''
        location = ''
        category = ''
        physical_activities = '' #fk
        prescription = []
        meal_plan = ''
        file_uploads = '' #fk
        other_med_condt = ''  
        appointment_date = ''
        approved = False
        description = ''


    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)
