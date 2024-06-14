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
    pregunta = request.json.get('pregunta')
    respuesta = request.json.get('respuesta')
    nropregunta = request.json.get('nropregunta')
    id_escala = request.json.get('id_escala')

    new_respuesta = UsuarioTest(id_test, id_paciente, pregunta, respuesta, nropregunta,id_escala)
    db.session.add(new_respuesta)
    db.session.commit()

    data={
        'message' : 'Test respondido',
        'status:' : 201
    }

    return make_response(jsonify(data),201)