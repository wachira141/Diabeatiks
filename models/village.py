#!/usr/bin/python3
"""
module contains Village model
"""
from models.base_model import BaseModel

class Village(BaseModel):
    """declaration of Village model"""
    name = ''
    location = ''
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)