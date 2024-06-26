from db import db

class Categoria(db.Model):
    __tablename__ = 'tb_categoria'
    id_categoria = db.Column(db.Integer, primary_key=True) 
    nombre = db.Column(db.String)

    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre