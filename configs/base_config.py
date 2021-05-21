import secrets
import os

class Base:
    FLASK_APP = os.environ.get("FLASK_APP")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = secrets.token_hex(16)

class Development(Base):
    FLASK_ENV= os.environ.get("FLASK_ENV")
    SQLALCHEMY_DATABASE_URI= os.environ.get("SQLALCHEMY_DATABASE_URI")
    
    pass

class Staging(Base):
    # DATABASE = "d3jbjhi84rcjka"
    # POSTGRES_USER = "vheobwrimkhkic"
    # POSTGRES_PASSWORD = "4474c1376841e6f99b13e75c35727e2b69f046cd349cb4f954ffd75fa8ac4e4e"
    # SQLALCHEMY_DATABASE_URI="postgres://vheobwrimkhkic:4474c1376841e6f99b13e75c35727e2b69f046cd349cb4f954ffd75fa8ac4e4e@ec2-34-254-69-72.eu-west-1.compute.amazonaws.com:5432/d3jbjhi84rcjka"
        
    pass

class Production(Base):
    pass