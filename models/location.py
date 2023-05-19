#!/usr/bin/python3

"""
module containing the location class
"""
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Location(BaseModel, Base):
    """declare class Location"""
    if storage_type == 'db_storage':
        __tablename__ = 'location'
        name = Column(String(60), nullable=False)
        subcounty = Column(String(60), ForeignKey('subcounty.id'), nullable=False)
        villages = relationship('Villages', backref='location')
    else:
        name = ''
        subcounty = ''
    # villages = []
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)
    