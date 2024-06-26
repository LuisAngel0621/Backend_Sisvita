from flask import Blueprint
from flask import request, make_response
from flask import jsonify
from models.Usuario import Usuario
from models.Diagnostico import Diagnostico
from schemas.Diagnostico_Schema import Diagnosticos_Schema
from models.UsuarioTipo import UsuarioTipo
from schemas.Usuario_schema import Usuario_Schema
from werkzeug.security import generate_password_hash
import secrets
import string
from db import db

evaluar = Blueprint('evaluar',__name__)

@evaluar.route('/EvaluarTest/<int:id_paciente>', methods = ['PUT']) #cambiar el nombre del CUS
def Guardar_datos(id_usutip):
    evaluacion = Diagnostico.query.get(id_usutip)
    comentario  = request.json.get('comentario')
    recomendacion = request.json.get('recomendacion')

    evaluacion.comentario = comentario
    evaluacion.recomendacion = recomendacion
    db.session.commit()

    data = {
        'message': 'Test evaluado',
        'status': 200
    }
    
    return make_response(jsonify(data),200)