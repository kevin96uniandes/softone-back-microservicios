import os
from flask import Blueprint, jsonify, request
from facade.facade import ClaveMaestraFacade

actions_blueprint = Blueprint('operations', __name__)

@actions_blueprint.route('/ping', methods=['GET'])
def healthcheck():
    return 'pong', 200

@actions_blueprint.route('/listar', methods = ['GET'])
def listar_claves_maestras():
    return jsonify({"data":ClaveMaestraFacade.obtener_claves_maestras()}), 200

@actions_blueprint.route('/crear', methods = ['POST'])
def crear_clave_maestra():
    return jsonify({"data": ClaveMaestraFacade.crear_clave_maestra(request.get_json())}), 200

