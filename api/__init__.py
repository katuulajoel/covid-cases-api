import os

from flask import Flask
from flask_cors import CORS

from api.v1 import blueprint as covid_api_v1
from config import app_config
from api.db import db, migrate
from api.ma import ma

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
flask_config = os.environ.get('FLASK_ENV', 'production')
app.config.from_object(app_config[flask_config])

db.init_app(app)
migrate.init_app(app, db)
ma.init_app(app)

app.register_blueprint(covid_api_v1)
