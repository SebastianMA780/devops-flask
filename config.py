import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://flask_user:flask_password@localhost:5432/flask_notes_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or "this-is-not-secret"

class TestConfig:
    SQLALCHEMY_DATABASE_URI = "postgresql://flask_user:flask_password@localhost:5432/flask_test_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "this-is-not-secret"
    TESTING = True

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    