import os

env = os.environ


class Config(object):
    SECRET_KEY = 'abc@123'
    DEBUG_TB_ENABLED = False

    # security
    SECURITY_PASSWORD_SALT = 'admin@123'

    # db
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


class ProdConfig(Config):
    EVN = 'prod'
    DEBUG = False
    DEBUG_TB_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = ''
