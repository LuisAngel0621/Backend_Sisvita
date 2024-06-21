from db import db
from models.Test import Test
from models.UsuarioTipo import UsuarioTipo

class UsuarioTest(db.Model):
    __tablename__ = 'tb_usuario_test'
    id_user_test = db.Column(db.Integer, primary_key=True) 
    id_test = db.Column(db.Integer, db.ForeignKey('tb_test.id_test'))
    id_paciente = db.Column(db.Integer, db.ForeignKey('tb_usuario_tipo.id_usutip'))
    id_escala = db.Column(db.Integer, db.ForeignKey('tb_escala.id_escala'))
    id_respuestas = db.Column(db.Integer, db.ForeignKey('tb_respuestas.id_respuestas'))
    id_preguntas = db.Column(db.Integer, db.ForeignKey('tb_preguntas.id_preguntas'))

    def __init__(self, id_test, id_paciente, id_escala, id_respuestas, id_preguntas):
        self.id_test = id_test
        self.id_paciente = id_paciente
        self.id_escala = id_escala
        self.id_respuestas = id_respuestas
        self.id_preguntas = id_preguntas