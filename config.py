import os
class Config:
    
    SECRET_KEY = 'hamisi'

    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hamisi:hamisi@localhost/pitch_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hamisi:hamisi@localhost/pitch'
    DEBUG = True
    


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
