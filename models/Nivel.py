from db import db

class Nivel(db.Model):
    __tablename__ = 'tb_nivel'
    id_nivel = db.Column(db.Integer, primary_key=True) 
    rang_min = db.Column(db.Integer)
    rang_max = db.Column(db.Integer)
    nivel_ansiedad = db.Column(db.String)

    def __init__(self, id_nivel, rang_min, rang_max, nivel_ansiedad):
        self.id_nivel = id_nivel
        self.rang_min = rang_min
        self.rang_max = rang_max
        self.nivel_ansiedad = nivel_ansiedad