'''
Flask sqlalchemy is a SQLAlchemy extension for Flask. 
https://flask-sqlalchemy.palletsprojects.com/en/2.x/
'''

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
