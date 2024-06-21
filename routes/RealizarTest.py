from flask import Blueprint
from flask import request, make_response
from flask import jsonify
from flask import jsonify
from models.UsuarioTest import UsuarioTest
from schemas.UsuarioTest_schema import Usuario_Test_Schema
from db import db

respuestas = Blueprint('respuestas', __name__)

@respuestas.route('/RealizarTest', methods = ['POST'])
def Guardar_Respuestas():
    id_test = request.json.get('id_test')
    id_paciente = request.json.get('id_paciente')
    id_escala = request.json.get('id_escala')
    id_respuestas = request.json.get('id_respuestas')
    id_preguntas = request.json.get('id_preguntas')

    new_respuesta = UsuarioTest(id_test, id_paciente, id_escala, id_respuestas, id_preguntas)
    db.session.add(new_respuesta)
    db.session.commit()

    data={
        'message' : 'Test respondido',
        'status:' : 201
    }

    return make_response(jsonify(data),201)