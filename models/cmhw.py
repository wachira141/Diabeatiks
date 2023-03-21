#!/usr/bin/python3
"""
contains class community_health_worker
"""
from models.registrant import Registrant

class CMHW(Registrant):
    """Declare class CMHW"""
    community = []
    def __init__(self, *args, **kwargs):
        """init this class"""
        super().__init__(*args, **kwargs)

