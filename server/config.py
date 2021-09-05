import os

class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # STORAGEACCOUNTURL = os.environ.get('STORAGEACCOUNTURL')
    # STORAGEACCOUNTKEY = os.environ.get('STORAGEACCOUNTKEY')
    # CONTAINERNAME = os.environ.get('CONTAINERNAME')
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'None'
    OAUTHLIB_INSECURE_TRANSPORT = True
    
class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    DEVELOPMENT = True
    
