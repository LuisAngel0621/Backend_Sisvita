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
    contraseña = request.json.get('contraseña')

    usuario = Usuario.query.filter_by(correoinstitucional = correoinstitucional).first()
    
    usuariotipo = UsuarioTipo.query.filter_by(id_usu = usuario.id_usu).first()
    print(usuariotipo.contraseña)
    if not usuario:
        return make_response(jsonify({"message": "Usuario no encontrado"}), 404)    
    

    # Verificar la contraseña
    if not check_password_hash(usuariotipo.contraseña, contraseña):
        return make_response(jsonify({"message": "Contraseña incorrecta"}), 401)

    data = {
        'codigo': "201",
        'mensaje': "Usuario Registrado",
    }   
    
    return make_response(jsonify(data), 200)    



