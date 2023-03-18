#!/usr/bin/python3
"""
module containing the prescription model
"""

from models.base_model import BaseModel

class Prescription(BaseModel):
    """Prescription model declaration"""
    user_id = ''
    drugs = []