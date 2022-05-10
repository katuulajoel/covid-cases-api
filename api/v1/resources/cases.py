from flask import request
from flask_restx import Namespace, Resource, fields

from api.v1.models.cases import CaseModel
from api.v1.schemas.cases import CaseSchema

namespace = Namespace('cases', 'Covid cases endpoints')

case_schema = CaseSchema()
cases_schema = CaseSchema(many=True)

case_model = namespace.model('Case', {
    'id': fields.Integer(
        readonly=True,
        description='Case identifier'
    ),
    'country': fields.String(
        readonly=True,
        description='Case country'
    ),
    'continent': fields.String(
        readonly=True,
        description='Case continent'
    ),
    'city': fields.String(
        readonly=True,
        description='Case city'
    ),
    'population': fields.Integer(
        readonly=True,
        description='Case population'
    ),
    'confirmed': fields.Integer(
        readonly=True,
        description='Confirmed cases'
    ),
    'deaths': fields.Integer(
        readonly=True,
        description='Deaths cases'
    ),
    'life_expectancy': fields.Float(
        readonly=True,
        description='Life expectancy'
    ),
    'updated_at': fields.DateTime(
        readonly=True,
        description='Last update date'
    ),
})

case_list_model = namespace.model('CaseList', {
    'cases': fields.Nested(
        case_model,
        description='List of covid cases',
        as_list=True
    ),
    'total_records': fields.Integer(
        description='Total number of records'
    )
})

summary_model = namespace.model('Summary', {
    'continent': fields.String(
        readonly=True,
        description='Case continent'
    ),
    'confirmed': fields.Integer(
        readonly=True,
        description='Confirmed cases'
    ),
    'deaths': fields.Integer(
        readonly=True,
        description='Deaths cases'
    )
})

@namespace.route('')
class Cases(Resource):
    '''Get covid cases and create new entities'''

    @namespace.response(500, 'Internal Server Error')
    @namespace.marshal_list_with(case_list_model)
    def get(self):
        cases = cases_schema.dump(CaseModel.find_all())
        return {'cases': cases, 'total_records': 10}, 200

@namespace.route('/<int:case_id>')
class Case(Resource):
    '''Get a specific case'''

    @namespace.response(404, 'Case not found')
    @namespace.response(500, 'Internal Server Error')
    @namespace.marshal_with(case_model)
    def get(self, case_id):
        case_data = CaseModel.find_by_id(case_id)
        if case_data:
            return case_schema.dump(case_data), 200
        return namespace.abort(404, 'Case not found')


@namespace.route('/country/<string:country>')
class CountryCase(Resource):
    '''Get cases by country'''

    @namespace.response(404, 'Case not found')
    @namespace.response(500, 'Internal Server Error')
    @namespace.marshal_with(case_model)
    def get(self, country):
        case_data = CaseModel.find_by_country(country)
        if case_data:
            return case_schema.dump(case_data), 200
        return namespace.abort(404, 'Case not found')


@namespace.route('/continent/<string:continent>')
class ContinentCases(Resource):
    '''Get cases by continent'''

    @namespace.response(500, 'Internal Server Error')
    @namespace.marshal_list_with(case_list_model)
    def get(self, continent):
        cases = cases_schema.dump(CaseModel.find_by_continent(continent))
        return {'cases': cases, 'total_records': 10}, 200

@namespace.route('/summary')
class CasesSummary(Resource):
    '''Get cases summary'''

    @namespace.response(500, 'Internal Server Error')
    @namespace.marshal_list_with(summary_model)
    def get(self):
        return cases_schema.dump(CaseModel.summary()), 200

@namespace.route('/countries_continents_list')
class CountriesContinentsList(Resource):
    '''Get cases summary'''

    @namespace.response(500, 'Internal Server Error')
    def get(self):
        countries = cases_schema.dump(CaseModel.get_countries())
        continents = cases_schema.dump(CaseModel.get_continents())
        countries_list = []
        continents_list = []
        for key in countries:
            countries_list.append(key['country'])
        for key in continents:
            if key['continent']:
                continents_list.append(key['continent'])


        return {'countries': countries_list, 'continents': continents_list}, 200
