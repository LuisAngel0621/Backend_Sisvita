from flask import Blueprint
from flask import request, make_response
from flask import jsonify
from flask import jsonify
from models.Usuario import Usuario
from models.UsuarioTipo import UsuarioTipo
from werkzeug.security import check_password_hash
from db import db

sesion = Blueprint('sesion', __name__)

@sesion.route('/Sesion', methods = ['POST']) #cambiar el nombre del CUS
def Validar_Sesion():
    correoinstitucional = request.json.get('correoinstitucional') 
    contrasenia = request.json.get('contrasenia')

    usuario = Usuario.query.filter_by(correoinstitucional = correoinstitucional)
    usuariotipo = UsuarioTipo.query.filter_by(id_usu = usuario.id_usu)

    if not usuario:
        return make_response(jsonify({"message": "Usuario no encontrado"}), 404)    
    

    # Verificar la contraseña
    if not check_password_hash(usuariotipo.contrasenia, contrasenia):
        return make_response(jsonify({"message": "Contraseña incorrecta"}), 401)
    
    return make_response(jsonify({"message": "Validación exitosa", "user": {"id": usuario.id_usu, "nombre": usuario.nombre}}), 200)    



