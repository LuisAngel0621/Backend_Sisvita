from flask import Blueprint,request, make_response,jsonify
from models.Preguntas import preguntaModel
from schemas.Pregunta_Schema import Tests_Schema
from db import db

preguntaBP = Blueprint('preguntas',__name__)

@preguntaBP.route('/ObtenerPreguntas', methods = ['GET']) 

def obtener_preguntas():

    preguntas = preguntaModel.query.all()
    preguntaSchema = Tests_Schema.dump(preguntas)

    data = {
        'preguntas': preguntaSchema,
        'status': 200
    }

    return make_response(jsonify(data),200)
