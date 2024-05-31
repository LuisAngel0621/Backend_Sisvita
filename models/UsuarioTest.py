from db import db
from models.Test import Test
from models.UsuarioTipo import UsuarioTipo

class UsuarioTest(db.Model):
    __tablename__ = 'tb_usuario_test'
    id_user_test = db.Column(db.Integer, primary_key=True) 
    id_test = db.Column(db.Integer, db.ForeignKey('tb_test.id_test'))
    id_paciente = db.Column(db.Integer, db.ForeignKey('tb_usuario_tipo.id_usutip'))
    pregunta = db.Column(db.String)
    respuesta = db.Column(db.Integer)
    nropregunta = db.Column(db.Integer)

    def __init__(self, id_test, id_paciente, pregunta, respuesta, nropregunta):
        self.id_test = id_test
        self.id_paciente = id_paciente
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.nropregunta = nropregunta