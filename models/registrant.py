#!/usr/bin/python3
"""
module containing the class Registrant
"""
from models.base_model import Base, BaseModel
import models
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Registrant(BaseModel):
    """class Registrant declaration"""
    if models.storage_type == 'db_storage':
        f_name = Column(String(60), nullable=False)
        l_name = Column(String(60), nullable=False)
        profile = Column(String(200))
        age = Column(Integer)
        email = Column(String(20), nullable=False)
        county = Column(String(20), nullable=False)
        subcounty = Column(String(20), nullable=False)
        location = Column(String(20), nullable=False)
    else:
        f_name = ''
        l_name = ''
        profile = ''
        age = 0
        email = ''
        county = ''
        subcounty = ''
        location = ''
    
    def __init__(self, *args, **kwargs):
        """init class Registrant"""
        super().__init__(*args, **kwargs)