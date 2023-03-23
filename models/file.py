#!/usr/bin/python3
"""module containing the single file"""

from models.base_model import BaseModel

class Single_file(BaseModel):
    """declare Single file"""
    name = '' #name of the file
    file_link = '' #link to where the file is stored. (ftp server)
    description = '' #details about the file
    file_id = '' # which file it belongs #fk
    def __init__(*args, **kwargs):
        """init single file and pass args to the superclass"""
        super().__init__(*args, **kwargs)