#!/usr/bin/python3
"""
module containing the Pharmacist class
"""
from models.registrant import Registrant
from models.base_model import Base
from models import storage_type
from sqlalchemy import Column, Boolean, String
from sqlalchemy.orm import relationship

class Pharmacist(Registrant, Base):
    if storage_type == 'db_storage':
        __tablename__ = 'pharmacist'
        description = Column(String(120))
        communities = relationship('community', backref='pharmacist')
        appointments = relationship('Appointments', backref='appointments')
        appointment_status = Column(Boolean, default=True)

    else:
        description = ''
        community = ''
        appointment_status = False
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)