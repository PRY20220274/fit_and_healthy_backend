class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    USER = "fitandhealthyadmin"
    PASSWORD = "RosarioRichard#98"
    SERVER = "fitandhealthy.mysql.database.azure.com"
    DATABASE = "fitandhealthy"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{SERVER}/{DATABASE}'
    SQLALCHEMY_ECHO = False
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = 'super secret'


class DevelopmentConfig(Config):
    USER = "root"
    PASSWORD = "pacheco98"
    SERVER = "localhost"
    DATABASE = "fit_and_healthy"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{SERVER}/{DATABASE}'
    SQLALCHEMY_ECHO = False
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = 'super secret'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///memory"
    SQLALCHEMY_ECHO = False


def register_config(app):
    config = DevelopmentConfig()
    app.config.from_object(config)
