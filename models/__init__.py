#!/usr/bin/python3

from os import getenv

storage_type = getenv('storage_type')

if storage_type == 'db_storage':
    from models.engine.db_storage import Db_storage
    storage = Db_storage()
else:
    from models.engine.filestorage import FileStorage
    storage = FileStorage()
    
storage.reload()