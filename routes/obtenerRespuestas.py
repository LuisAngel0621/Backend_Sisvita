from flask import Blueprint,request, make_response,jsonify
from models.Respuestas import respuestasModel
from schemas.Respuestas_Schema import Tests_Schema
from db import db

respuestaBP = Blueprint('respuestasTest',__name__)

@respuestaBP.route('/ObtenerRespuestas', methods = ['GET']) 

def obtener_preguntas():

    repuestas = respuestasModel.query.all()
    repuestaSchema = Tests_Schema.dump(repuestas)

    data = {
        'preguntas': repuestaSchema,
        'status': 200
    }

    return make_response(jsonify(data),200)