from db import db

class Test(db.Model):
    __tablename__ = 'tb_categoria'
    id_categoria = db.Column(db.Integer, primary_key=True) 
    nombre = db.Column(db.String)

    def __init__(self, id_escala, nombre):
        self.id_escala = id_escala
        self.nombre = nombre