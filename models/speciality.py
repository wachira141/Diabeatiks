#!/usr/bin/python3

"""
module containing the Speciality class declaration
"""

from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String

class Speciality(BaseModel, Base):
    """class Speciality Declaration"""
    if storage_type == 'db_storage':
        __tablename__ = 'speciality'
        description = Column(String(20), nullable=False)
    else:
         description = ''

    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)