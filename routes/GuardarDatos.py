from flask import Blueprint, render_template as request, make_response
from flask import jsonify
from models.Usuario import Usuario
from schemas.Usuario_schema import Usuario_Schema
from db import db

usuario = Blueprint('usuarios',__name__)

@usuario.route('/GuardarDatos', methods = ['POST'])
def Guardar_datos():
    nombres = request.json.get('nombres')
    apellidos = request.json.get('apellidos')
    correoconst = request.json.get('correoconst')
    edad = request.json.get('edad')
    sexo = request.json.get('sexo')
    estadocivil = request.json.get('estadocivil')
    ocupacion = request.json.get('ocupacion')

    new_usuario = Usuario(nombres, apellidos, correoconst, edad, sexo, estadocivil, ocupacion)
    db.session.add(new_usuario)
    db.session.commit()

    data = {
        'message': 'Nuevo Usuario registrado',
        'status': 201
    }

    return make_response(jsonify(data),201)