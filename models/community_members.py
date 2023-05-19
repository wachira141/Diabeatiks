#!/usr/bin/python3
""""
contains class Community_members model
"""
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Boolean
from datetime import datetime
from models.base_model import BaseModel, Base
from models import storage_type

class Community_members(BaseModel, Base):
    """Community_members class definition"""
    if storage_type == 'db_storage':
        __tablename__ = 'community_members'
        user_id = Column(String(60), ForeignKey('patient.id'),nullable=False)
        community_id = Column(String(60), ForeignKey('community.id'), nullable=False)
        join_date = Column(DateTime, default=datetime.utcnow)
        member_approved = Column(Boolean, default=False)
    else:  
        user_id = ''
        community_id = ''
        join_date = ''
        member_approved = ''


    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)