from os import environ


class Config(object):
    TESTING = False

    SPORTS_API_URL = environ.get("SPORTS_API_URL")
    SPORTS_API_KEY = environ.get("SPORTS_API_KEY")


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
