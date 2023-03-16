#!/usr/bin/python3
"""
contains class Drugs model
"""
from models.base_model import BaseModel

class Drugs(BaseModel):
    """declare class Drugs"""
    name = ''
    price = float
    bought_at = '' #shop bought at
    description = ''
    side_effects = ''