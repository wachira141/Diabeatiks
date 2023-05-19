#!/usr/bin/python3

"""
module containing the subcounty model
"""

from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, Integer, Float, String, ForeignKey

class Subcounty(BaseModel, Base):
    """class Subcounty declaration"""
    if storage_type == 'db_storage':
        __tablename__ = 'subcounty'
        name = Column(String(20), nullable=False)
        county = Column(String(60), ForeignKey('county.id'), nullable=False)
    else:
        name=''
        county=''
        
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)