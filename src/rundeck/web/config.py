import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = False
    SECRET_KEY = 'rundec-cli'
    RUNDECK_USERNAME = os.environ.get('RUNDECK_USERNAME', 'admin')
    RUNDECK_PASSWORD = os.environ.get('RUNDECK_PASSWORD', 'admin')
    RUNDECK_URL = os.environ.get('RUNDECK_URL', 'http://localhost:4440')


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
