from flask import Blueprint
from flask import request, make_response
from flask import jsonify
from flask import jsonify
from models.Diagnostico import Diagnostico
from models.Nivel import Nivel
from schemas.Nivel_Schema import Niveles_Schema,Nivel_Schema
from schemas.Diagnostico_Schema import Diagnostico_Schema,Diagnosticos_Schema
from db import db

vigilancia = Blueprint('vigilancia', __name__)

@vigilancia.route('/RealizarVigilancia/<id>', methods = ['GET'])
def TestRealizadosEspecifico(id):
    Evatest = Diagnostico.query.filter_by(id_diag=id).first()
    if Evatest:
        res = Diagnostico_Schema.dump(Evatest)
        response ={
            'success': True,
            'data': res
        }    
        return make_response(jsonify(response),200)
    else:
        response ={
            'success': True,
            'message': 'Diagnostico no encontrado'
        }
        return make_response(jsonify(response), 404)


    
@vigilancia.route('/ObtenerNivel', methods = ['GET'])
def ObtenerNivel():
    niveles = Nivel.query.all()
    nivelesSchemas = Niveles_Schema.dump(niveles)
    data = {
        'niveles': nivelesSchemas,
        'status': 201
    }

    return make_response(jsonify(data),201)

    
@vigilancia.route('/ObtenerNivel/<id>', methods = ['GET'])
def ObtenerNivelEspecifico(id):
    niveltes = Nivel.query.filter_by(id_nivel=id).first()
    if niveltes:
        res = Nivel_Schema.dump(niveltes)
        data = {
            'niveles': res,
            'status': 201
        }
        return make_response(jsonify(data),201)
    else:
        response ={
            'success': True,
            'message': 'Diagnostico no encontrado'
        }
        return make_response(jsonify(response), 404)



@vigilancia.route('/RealizarVigilancia', methods = ['GET'])
def TestRealizados():
    Evatest = Diagnostico.query.all()
    res = Diagnosticos_Schema.dump(Evatest)
    
    response ={
        'success': True,
        'data': res
    }    
    return make_response(jsonify(response),200)
