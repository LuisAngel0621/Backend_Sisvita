from db import db

class Diagnostico(db.Model):
    __tablename__ = 'tb_diagnostico'
    id_diag = db.Column(db.Integer, primary_key=True)
    id_usutip = db.Column(db.Integer,db.ForeignKey('tb_usuario_tipo.id_usutip'))
    id_nivel = db.Column(db.Integer,db.ForeignKey('tb_nivel.id_nivel'))
    nombres = db.Column(db.String)
    apellidos = db.Column(db.String)
    tipo_test = db.Column(db.String)
    puntaje = db.Column(db.Integer)
    comentario = db.Column(db.String)
    recomendacion = db.Column(db.String)
    notificacion = db.Column(db.Boolean)
    fecha_test = db.Column(db.Date)

    def __init__(self, id_diag, id_usutip, nombres, apellidos, tipo_test, id_nivel, puntaje, comentario, recomendacion, notificacion, fecha_test):
        self.id_diag = id_diag
        self.id_usutip = id_usutip
        self.nombres = nombres
        self.apellidos = apellidos
        self.tipo_test = tipo_test
        self.id_nivel = id_nivel
        self.puntaje = puntaje
        self.comentario = comentario
        self.recomendacion = recomendacion
        self.notificacion = notificacion
        self.fecha_test = fecha_test