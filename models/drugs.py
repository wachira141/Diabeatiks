#!/usr/bin/python3
"""
contains class Drugs model
"""
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, Integer, ForeignKey, String

# class Drugs(BaseModel):
#     """declare class Drugs"""
#     name = ''
#     price = float
#     bought_at = '' #shop bought at
#     description = ''
#     side_effects = ''

class Drugs(BaseModel, Base):
    """declare class Drugs"""
    if storage_type == 'db_storage':
        __tablename__ = 'drug'
        name = Column(String(60), nullable=False)
        category=Column(String(60), nullable=False)
        d_group = Column(String(20), nullable=False)
        age = Column(Integer, nullable=False)
        dosage = Column(String(102), nullable=False)
        frequency = Column(String(102), nullable=False)
        condition = Column(String(200), nullable=False)
        known_side_effects = Column(String(200), nullable=False)
        prescription = Column(String(60), ForeignKey('prescription.id'), nullable=False)
    else:
        name = ''
        category=''
        d_group = ''
        age = ''
        dosage = ''
        frequency = ''
        condition = ''
        known_side_effects = ''

    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)