from db import db

class UsuarioTest(db.Model):
    __tablename__ = 'tb_usuario_test'
    id_user_test = db.Column(db.Integer, primary_key=True) 
    id_test = db.Column(db.Integer, db.ForeignKey('Test.id_test'))
    id_paciente = db.Column(db.Integer, db.ForeignKey('UsuarioTipo.id_usutip'))
    pregunta = db.Column(db.String)
    respuesta = db.Column(db.String)
    nropregunta = db.Column(db.Integer)
    
    def __init__(self, id_test, id_paciente, pregunta, respuesta, nropregunta):
        self.id_test = id_test
        self.id_paciente = id_paciente
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.nropregunta = nropregunta