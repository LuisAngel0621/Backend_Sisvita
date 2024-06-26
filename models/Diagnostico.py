from db import db

class Diagnostico(db.Model):
    __tablename__ = 'tb_diagnostico'
    id_diag = db.Column(db.Integer, primary_key=True)
    id_usutip = db.Column(db.Integer,db.ForeignKey('tb_usuario_tipo.id_usutip')) 
    id_user_test = db.Column(db.Integer,db.ForeignKey('tb_usuario_test.id_user_test'))
    id_nivel = db.Column(db.Integer,db.ForeignKey('tb_nivel.id_nivel'))
    puntaje = db.Column(db.Integer)
    comentario = db.Column(db.String)
    recomendacion = db.Column(db.String)
    notificacion = db.Column(db.Boolean)

    def __init__(self, id_diag, id_usutip, id_user_test, id_nivel, puntaje, comentario, recomendacion, notificacion):
        self.id_diag = id_diag
        self.id_usutip = id_usutip
        self.id_user_test = id_user_test
        self.id_nivel = id_nivel
        self.puntaje = puntaje
        self.comentario = comentario
        self.recomendacion = recomendacion
        self.notificacion = notificacion