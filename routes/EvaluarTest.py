from flask import Blueprint
from flask import request, make_response
from flask import jsonify
from models.Usuario import Usuario
from models.Diagnostico import Diagnostico
from schemas.Diagnostico_Schema import Diagnosticos_Schema
from models.UsuarioTipo import UsuarioTipo
from schemas.Usuario_schema import Usuario_Schema
from werkzeug.security import generate_password_hash
import smtplib
from email.mime.text import MIMEText

import secrets
import string
from db import db

evaluar = Blueprint('evaluar',__name__)

@evaluar.route('/EvaluarTest/<int:id_diag>', methods = ['PUT']) #cambiar el nombre del CUS
def Guardar_datos(id_diag):
    evaluacion = Diagnostico.query.get(id_diag)
    id_usutip = request.json.get('id_usutip')       #ID del especialista
    comentario  = request.json.get('comentario')
    recomendacion = request.json.get('recomendacion')

    evaluacion.id_usutip = id_usutip                
    evaluacion.comentario = comentario
    evaluacion.recomendacion = recomendacion
    db.session.commit()

    data = {
        'message': 'Test evaluado',
        'status': 201
    }
    
    return make_response(jsonify(data),201)

@evaluar.route('/NotificarResultado', methods = ['POST']) #cambiar el nombre del CUS
def Notificar_resultados():

    correo_especialista = request.json.get("correo_especialista")
    contraseña = request.json.get("contraseña")
    correo_paciente = request.json.get("correo_paciente")
    comentario  = request.json.get('comentario')
    recomendacion = request.json.get('recomendacion')

    servidor = smtplib.SMTP("smtp.gmail.com",587)
    servidor.starttls()
    servidor.login(correo_especialista,contraseña)
    msg = MIMEText(f"Comentario:{comentario}\nRecomendacion: {recomendacion}")

    msg["From"] = correo_especialista
    msg["To"] = correo_paciente
    msg["Subject"] = "Evaluación del Test"

    servidor.sendmail(correo_especialista,correo_paciente,msg.as_string())
    servidor.quit()

    
    data = {
        'message': 'Evaluación notificada',
        'status': 201
    }
    
    return make_response(jsonify(data),201)