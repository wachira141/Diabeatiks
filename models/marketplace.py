#!/usr/bin/python3
"""
module containin the marketplace model
"""

from models.base_model import BaseModel

class Market_place(BaseModel):
    """Market_place class declaration"""
    user_id = ''
    name = ''
    description = ''
    price = float
    category = ''