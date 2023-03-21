#!/usr/bin/python3
"""
module contains the meal plan class
"""

from models.base_model import BaseModel

class Meal(BaseModel):
    """Declare Meal class"""
    break_fast = ''
    lunch = ''
    supper = ''
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)