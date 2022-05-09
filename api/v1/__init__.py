from flask import Blueprint
from flask_restx import Api
from api.v1.resources.cases import namespace as cases_ns

blueprint = Blueprint('covid_cases_api', __name__, url_prefix='/cases_api')

api_extension = Api(blueprint,
    title='Covid-19 Cases API',
    version='1.0',
    description='Application is a RESTful API that provides access to the \
        static data from the COVID-19 project.',
    doc='/docs'
)

api_extension.add_namespace(cases_ns)