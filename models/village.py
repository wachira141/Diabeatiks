#!/usr/bin/python3
"""
module contains Village model
"""
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, Integer, Float, String, ForeignKey

class Village(BaseModel):
    """declaration of Village model"""
    if storage_type == 'db_storage':
        __tablename__ = 'village'
        name = Column(String(20), nullable=False)
        location = Column(String(60), ForeignKey('location.id'), nullable=False)
    else:
       name = ''
       location = ''
       
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)