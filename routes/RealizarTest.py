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
    data = request.json
    id_test = data.get('id_test')
    id_paciente = data.get('id_paciente')
    answers = data.get('answers')

    
    for answer in answers:
        id_escala = answer.get('id_escala')
        id_respuestas = answer.get('id_respuestas')
        id_preguntas = answer.get('id_preguntas')

        if not id_preguntas or not id_respuestas:
            return jsonify({'error': 'Cada respuesta debe contener question_id y respuesta'}), 400
        new_test = UsuarioTest(id_test = id_test,id_paciente=id_paciente,id_escala = id_escala, id_respuestas=id_respuestas, id_preguntas=id_preguntas)
        db.session.add(new_test)
    db.session.commit()
    return make_response(jsonify({'message': 'Registro de Test exitoso'}), 201)




