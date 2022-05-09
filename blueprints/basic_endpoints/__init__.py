from flask import Blueprint, request

blueprint = Blueprint('api', __name__, url_prefix='/basic_api')

@blueprint.route('/hello_world')
def hello_world():
    return {'message': 'Hello, World!'}

@blueprint.route('/entities', methods=['GET', 'POST'])
def entities():
    if request.method == 'GET':
        return {
            'message': 'This endpoint should return a list of entities.',
            'method': request.method,
        }
    if request.method == 'POST':
        return {
            'message': 'This endpoint should create a new entity.',
            'method': request.method,
            'body': request.json
        }

@blueprint.route('/entities/<int:entity_id>', methods=['GET', 'PUT', 'DELETE'])
def entity(entity_id):
    if request.method == 'GET':
        return {
            'id': entity_id,
            'message': 'This endpoint should return an entity.',
            'method': request.method
        }
    if request.method == 'PUT':
        return {
            'id': entity_id,
            'message': 'This endpoint should update an entity.',
            'method': request.method,
            'body': request.json
        }
    if request.method == 'DELETE':
        return {
            'id': entity_id,
            'message': 'This endpoint should delete an entity.',
            'method': request.method
        }
        