from pydoc import describe
from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus

namespace = Namespace('entities', 'Entities fake endpoints')

entity_model = namespace.model('Entity', {
    'id': fields.Integer(
        readonly=True,
        description='Entity identifier'
    ),
    'name': fields.String(
        required=True,
        description='Entity name'
    ),
})

entity_list_model = namespace.model('EntityList', {
    'entities': fields.Nested(
        entity_model,
        description='List of entities',
        as_list=True
    ),
    'total_records': fields.Integer(
        description='Total number of records'
    )
})

entity_example = {'id': 1, 'name': 'Entity name'}

@namespace.route('')
class Entities(Resource):
    '''Get entities list and create new entities'''

    @namespace.response(500, 'Internal Server Error')
    @namespace.marshal_list_with(entity_list_model)
    def get(self):
        '''List with all the entities'''
        entity_list = [entity_example]

        return {'entities': entity_list, 'total_records': len(entity_list)}

    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(500, 'Internal Server Error')
    @namespace.expect(entity_model)
    @namespace.marshal_with(entity_model, code=200)
    def post(self):
        '''Create a new entity'''

        if request.json['name'] == 'Entity name':
            namespace.abort(400, 'Entity with the given name already exists')

        return entity_example, 201

@namespace.route('/<int:entity_id>')
class Entity(Resource):
    '''Read, update and delete a specific entity'''

    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server Error')
    @namespace.marshal_with(entity_model)
    def get(self, entity_id):
        '''Get entity_example information'''

        return entity_example

    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server Error')
    @namespace.expect(entity_model, validate=True)
    @namespace.marshal_with(entity_model)
    def put(self, entity_id):
        '''Update entity_example information'''

        if request.json['name'] == 'Entity name':
            namespace.abort(400, 'Entity with the given name already exists')

        return entity_example

    @namespace.response(204, 'Request Sucess (No Content)')
    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server Error')
    def delete(self, entity_id):
        '''Delete entity_example information'''

        return None, 204

