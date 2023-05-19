#!/usr/bin/python3
"""
contains Community model
"""
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import storage_type

class Community(BaseModel, Base):
    if storage_type == 'db_storage':
        __tablename__ = 'community'
        created_by = Column(String(60), ForeignKey('cmhw.id'),nullable=False)
        members = relationship('community_members')
    else:
        created_by = ''
        members = []


    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)