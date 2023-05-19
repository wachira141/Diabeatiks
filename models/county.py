#!/usr/bin/python
"""
module containing the County model
"""
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class County(BaseModel, Base):
    """declare class County"""
    if storage_type == 'db_storage':
        __tablename__ = 'county'
        name = Column(String(60), nullable=False)
        subcounties = relationship('Subcounty', backref='subcounty')
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)
