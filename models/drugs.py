#!/usr/bin/python3
"""
contains class Drugs model
"""
from models.base_model import BaseModel

# class Drugs(BaseModel):
#     """declare class Drugs"""
#     name = ''
#     price = float
#     bought_at = '' #shop bought at
#     description = ''
#     side_effects = ''

class Drugs(BaseModel):
    """declare class Drugs"""
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