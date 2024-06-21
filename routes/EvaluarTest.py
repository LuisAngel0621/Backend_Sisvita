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
def Guardar_datos(id_usu):
    evaluacion = Diagnostico.query.get(id_usu)
    resultado = request.json.get('resultado')
    diagnostico = request.json.get('diagnostico')

    evaluacion.resultado = resultado
    evaluacion.diagnostico = diagnostico
    db.session.commit()

    data = {
        'message': 'Recaudacion actualizada',
        'status': 200
    }
    
    return make_response(jsonify(data),200)
                                   
@evaluar.route('/VisualizarResultados', methods = ['GET'])
def Visualizar_datos():
    usuarios_eval = Diagnostico.query.all()
    resultado = Diagnosticos_Schema.dump(usuarios_eval)
    response ={
       'success': True,
        'data': resultado
    }    
    return make_response(jsonify(response),200)




