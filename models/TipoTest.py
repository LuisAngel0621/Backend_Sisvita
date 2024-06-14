from db import db

class Test(db.Model):
    __tablename__ = 'tb_tipotest'
    id_tipotest = db.Column(db.Integer, primary_key=True) 
    nombre = db.Column(db.String)
    cantpregunta = db.Column(db.Integer)

    def __init__(self, id_tipotest, nombre, cantpregunta):
        self.id_tipotest = id_tipotest
        self.nombre = nombre
        self.cantpregunta = cantpregunta