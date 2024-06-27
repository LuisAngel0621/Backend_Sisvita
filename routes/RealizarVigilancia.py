from flask import Blueprint
from flask import request, make_response
from flask import jsonify
from flask import jsonify
from models.Diagnostico import Diagnostico
from models.Nivel import Nivel
from schemas.Nivel_Schema import Niveles_Schema
from schemas.Diagnostico_Schema import Diagnosticos_Schema
from db import db

vigilancia = Blueprint('vigilancia', __name__)

@vigilancia.route('/RealizarVigilancia', methods = ['GET'])
def TestRealizados():
    usuarios_eval = Diagnostico.query.all()
    resultado = Diagnosticos_Schema.dump(usuarios_eval)
    response ={
       'success': True,
        'data': resultado
    }    
    return make_response(jsonify(response),201)

@vigilancia.route('/ObtenerNivel', methods = ['GET'])
def ObtenerNivel():
    niveles = Nivel.query.all()
    nivelesSchemas = Niveles_Schema.dump(niveles)
    data = {
        'niveles': nivelesSchemas,
        'status': 201
    }

    return make_response(jsonify(data),201)
