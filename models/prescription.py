#!/usr/bin/python3
"""
module containing the prescription model
"""

from models.base_model import BaseModel

class Prescription(BaseModel):
    """Prescription model declaration"""
    user_id = '' #user/ owner of the presc
    drugs = []  #drugs
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)