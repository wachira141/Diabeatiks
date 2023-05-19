#!/usr/bin/python3
"""
module to declare files model
"""
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

class Files(BaseModel, Base):
    """class Files declaration"""
    if storage_type == 'db_storage':
        __tablename__ = 'files'
        user = Column(String(60), ForeignKey('patient.id'), nullable=False)
        destination = Column(String(60), ForeignKey('doctor.id'), nullable=False)
        file = relationship('Single_file', backref='files')
    else:
        user: str = ''        #sender
        destination: str = '' #to whom the file is sent to
        
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)