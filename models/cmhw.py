#!/usr/bin/python3
"""
contains class community_health_worker
"""
from models.registrant import Registrant
from models.base_model import Base
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models import storage_type

class CMHW(Registrant, Base):
    """Declare class CMHW"""
    if storage_type == 'db_storage':
        __tablename__ = 'cmhw'
        community = relationship('community.id', backref='cmhw')
    else:
        community = []
        
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)

