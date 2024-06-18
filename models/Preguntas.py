from db import db

class preguntaModel(db.Model):
    __tablename__ = 'tb_preguntas'
    
    id_preguntas = db.Column(db.Integer, primary_key=True) 
    descripcion = db.Column(db.String)

    def __init__(self, id_preguntas, descripcion):
        self.id_preguntas = id_preguntas
        self.descripcion = descripcion
 