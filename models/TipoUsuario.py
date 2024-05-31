from db import db

class TipoUsuario(db.Model):
    __tablename__ = 'tb_tipousuario'
    id_tipo = db.Column(db.Integer, primary_key=True) 
    tipo = db.Column(db.Integer)
    estado = db.Column(db.Integer)
    
    def __init__(self, id_tipo, tipo, estado):
        self.id_tipo = id_tipo
        self.tipo = tipo
        self.estado = estado