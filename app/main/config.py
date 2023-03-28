import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False

class DevConfig(Config): 
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = dict(
        dev=DevConfig, 
        test=TestingConfig,
        prod=ProductionConfig
        )


