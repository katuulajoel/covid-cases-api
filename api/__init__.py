import os

from flask import Flask

from blueprints.basic_endpoints import blueprint as basic_endpoint
from blueprints.jinja_endpoint import blueprint as jinja_template_blueprint
from blueprints.documented_endpoints import blueprint as documented_endpoint
from api.v1 import blueprint as covid_api_v1
from config import app_config
from api.db import db, migrate
from api.ma import ma

def create_app(config_name):
    app = Flask(__name__)
    flask_config = os.environ.get('FLASK_ENV')
    app.config.from_object(app_config[flask_config])

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    app.register_blueprint(basic_endpoint)
    app.register_blueprint(jinja_template_blueprint)
    app.register_blueprint(documented_endpoint)
    app.register_blueprint(covid_api_v1)

    return app

if __name__ == "__main__":
    create_app.run(debug=True)

