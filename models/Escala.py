from db import db

class Test(db.Model):
    __tablename__ = 'tb_escala'
    id_escala = db.Column(db.Integer, primary_key=True) 
    descripcion = db.Column(db.String)

    def __init__(self, id_escala, descripcion):
        self.id_escala = id_escala
        self.descripcion = descripcion