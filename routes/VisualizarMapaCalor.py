from flask import Blueprint
from flask import request, make_response
from flask import jsonify
from flask import jsonify
from models.Ubigeo import Ubigeo
from schemas.Ubigeo_Schema import Ubigeos_Schema
from db import db

mapacalor = Blueprint('mapacalor', __name__)

@mapacalor.route('/VisualizarMapa', methods = ['GET'])
def MapaCalor():
    ubigeo_eval = Ubigeo.query.all()
    resultado = Ubigeos_Schema.dump(ubigeo_eval)
    response ={
       'success': True,
        'data': resultado
    }    
    return make_response(jsonify(response),201)