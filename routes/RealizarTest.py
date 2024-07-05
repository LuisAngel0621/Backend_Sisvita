from flask import Blueprint
from flask import request, make_response
from flask import jsonify
from flask import jsonify
from models.UsuarioTest import UsuarioTest
from models.Diagnostico import Diagnostico
from models.Respuestas import Respuestas
from models.Preguntas import Preguntas
from models.Escala import Escala
from models.Nivel import Nivel
from schemas.Escala_Schema import Escalas_Schema
from schemas.Respuestas_Schema import Respuestas_Schema
from schemas.Pregunta_Schema import Preguntas_Schema
from schemas.Nivel_Schema import Niveles_Schema
from schemas.UsuarioTest_schema import Usuario_Test_Schema
from db import db
from datetime import datetime

respuestas = Blueprint('respuestas', __name__)

@respuestas.route('/RealizarTest', methods = ['POST'])
def Guardar_Respuestas():
    data = request.json
    id_test = data.get('id_test')
    id_paciente = data.get('id_paciente')
    answers = data.get('answers')
    fecha_test = datetime.now()
    for answer in answers:
        id_escala = answer.get('id_escala')
        id_respuestas = answer.get('id_respuestas')
        id_preguntas = answer.get('id_preguntas')

        if not id_preguntas or not id_respuestas:
            return jsonify({'error': 'Cada respuesta debe contener question_id y respuesta'}), 400
        new_test = UsuarioTest(id_test = id_test,id_paciente=id_paciente,id_escala = id_escala, id_respuestas=id_respuestas, id_preguntas=id_preguntas,fecha_test = fecha_test)
        db.session.add(new_test)
    db.session.commit()

    id_user_test = db.session.query(UsuarioTest).order_by(UsuarioTest.id_user_test.desc()).first().id_user_test
    return make_response(jsonify({'message': 'Registro de Test exitoso', 'id_user_test': id_user_test}), 201)


@respuestas.route('/ObtenerPreguntas', methods = ['GET'])
def obtener_preguntas():

    preguntas = Preguntas.query.all()
    preguntaSchema = Preguntas_Schema.dump(preguntas)

    data = {
        'preguntas': preguntaSchema,
        'status': 201
    }

    return make_response(jsonify(data),201)

@respuestas.route('/ObtenerRespuestas', methods = ['GET'])
def obtener_respuestas():

    respuestas = Respuestas.query.all()
    respuestasSchema = Respuestas_Schema.dump(respuestas)

    data = {
        'respuestas': respuestasSchema,
        'status': 201
    }

    return make_response(jsonify(data),201)

@respuestas.route('/ObtenerEscala', methods = ['GET'])
def obtener_escala():

    escalas = Escala.query.all()
    escalasSchema = Escalas_Schema.dump(escalas)

    data = {
        'escalas': escalasSchema,
        'status': 201
    }

    return make_response(jsonify(data),201)

@respuestas.route("/ObtenerNivel", methods = ['GET'])
def obtener_nivel():
    niveles = Nivel.query.all()
    nivelesSchema = Niveles_Schema.dump(niveles)

    data = {
        'niveles': nivelesSchema,
        'status': 201
    }

    return make_response(jsonify(data),201)

@respuestas.route('/SumaPuntaje/<int:id_paciente>', methods = ['GET'])
def suma_puntaje(id_paciente):
    suma_id_escala = db.session.query(db.func.sum(UsuarioTest.id_escala)).filter_by(id_paciente=id_paciente).scalar()
    data ={
        'success': True,
        'suma': suma_id_escala
    }
    return make_response(jsonify(data),201)  

@respuestas.route('/ResultadoTest', methods = ['POST'])
def resultado_test():
    id_user_test = request.json.get('id_user_test')
    id_nivel = request.json.get('id_nivel') 
    puntaje = request.json.get('puntaje')
    comentario = request.json.get('comentario')
    recomendacion = request.json.get('recomendacion')
    notificacion = False

    new_diagnostico = Diagnostico(id_user_test,id_nivel,puntaje,comentario,recomendacion,notificacion)
   
    db.session.add(new_diagnostico)
    db.session.commit()

    id_diag = db.session.query(Diagnostico).order_by(Diagnostico.id_diag.desc()).first().id_diag

    data = {
        'success': True,
        'id_diag': id_diag
    }
    
    return make_response(jsonify(data),201)



