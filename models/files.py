#!/usr/bin/python3
"""
module to declare files model
"""
from models.base_model import BaseModel

class Files(BaseModel):
    """class Files declaration"""
    user_id = ''
    sent_to = ''
    files = []