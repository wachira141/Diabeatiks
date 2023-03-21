#!/usr/bin/python3
""""
contains class Community_members model
"""

from models.base_model import BaseModel

class Community_members(BaseModel):
    """Community_members class definition"""
    user_id = ''
    community_id = ''
    join_date = ''
    member_approved = ''
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)