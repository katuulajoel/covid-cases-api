import os

from flask import Flask

from api.v1 import blueprint as covid_api_v1
from config import app_config
from api.db import db, migrate
from api.ma import ma

app = Flask(__name__)
flask_config = os.environ.get('FLASK_ENV')
app.config.from_object(app_config[flask_config])

db.init_app(app)
migrate.init_app(app, db)
ma.init_app(app)

app.register_blueprint(covid_api_v1)
