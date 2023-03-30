#!/usr/bin/python3
"""
module to declare files model
"""
from models.base_model import BaseModel

class Files(BaseModel):
    """class Files declaration"""
    user = '' #sender
    sent_to = '' #to whom the file is sent to 
    # files = []
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)