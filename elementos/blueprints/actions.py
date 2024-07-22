import os
from flask import Blueprint, jsonify, request
from facade.facade import ElementoFacade

actions_blueprint = Blueprint('operations', __name__)

@actions_blueprint.route('/ping', methods=['GET'])
def healthcheck():
    return 'pong', 200

@actions_blueprint.route('/listar', methods = ['GET'])
def list_elementos():
    return jsonify(ElementoFacade.get_elementos()), 200

@actions_blueprint.route('/crear', methods = ['POST'])
def crear_elementos():
    return ElementoFacade.create_elemento(request.get_json()), 200

