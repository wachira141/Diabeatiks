#!/usr/bin/python3
"""
contains Daetician class model
"""
from models.registrant import Registrant
from models.base_model import Base
from models import storage_type
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

class Daetician(Registrant, Base):
    """ class Daetician"""
    if storage_type == 'db_storage':
        __tablename__ = 'daetician'

        communities =relationship('Community', backref='community')
        appointments = relationship('Appointments', backref='appointments')
        appointment_status = Column(Boolean, default=True)
        # facility_id = ''
    else:
        community =''
        appointment_status = True
        # facility_id = ''

    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)