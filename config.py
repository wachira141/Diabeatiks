#!/usr/bin/env python3


class Config:
    '''
    Base class for configuration environments
    '''
    #storage type
    #database name, password, host, user
    STORAGE_TYPE = 'db_storage'
    DEBUG= False
    FLASK_ENV = 'production'
    DIABETICS_DB = 'diabetics_dev_db'
    DIABETICS_USERNAME = 'root'
    DIABETICS_PASSWORD = '#diabetics1234'
    DIABETICS_HOSTNAME = 'host'
    SQLALCHEMY_ECHO = True


class DevConfig(Config):
    '''development configuration'''
    FLASK_ENV = 'development'
    STORAGE_TYPE = 'file_storage'
    DEBUG= True
    DIABETICS_DB = 'diabetics_devDb'

class ProductionConfig(Config):
    '''production configurations'''

class TestConfig(Config):
    '''test environment configuration'''
    DIABETICS_DB = 'diabetics_testDb'
    FLASK_ENV = 'testing'