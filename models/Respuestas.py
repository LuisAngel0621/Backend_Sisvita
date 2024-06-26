from db import db

class Respuestas(db.Model):
    __tablename__ = 'tb_respuestas'
    
    id_respuestas = db.Column(db.Integer, primary_key=True) 
    descripcion = db.Column(db.String)

    def __init__(self, id_respuestas, descripcion):
        self.id_respuestas = id_respuestas
        self.descripcion = descripcion