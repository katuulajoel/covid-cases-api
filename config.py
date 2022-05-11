from dotenv import load_dotenv
load_dotenv()

import os

class Config:
    """
    Common configurations
    """

    SECRET_KEY = os.environ.get('SECRET_KEY')
    TESTING = False
    DEBUG = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgres://xcnhueiaxsostk:1a007886680381b935a35cab5a350005143fd846a42cd89a198b6404a438d673@ec2-18-210-64-223.compute-1.amazonaws.com:5432/d5bhi9en1h3oe1'


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
