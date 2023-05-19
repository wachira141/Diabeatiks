#!/usr/bin/python3
"""
module containing the prescription model
"""

from models.base_model import Base, BaseModel
from models import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Prescription(BaseModel, Base):
    """Prescription model declaration"""
    if storage_type == 'db_storage':
        __tablename__ = 'prescription'
        user_id = Column(String(60), ForeignKey('patient.id'), nullable=False)
        drugs = relationship('drugs.id', backref='prescription')
        appointment = Column(String(50), ForeignKey('appointments.id'), nullable=False)

    else:
        user_id = ''      #user/ owner of the presc
        drugs = []        #drugs


    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)