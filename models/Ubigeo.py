from db import db

class Ubigeo(db.Model):
    __tablename__ = 'tb_ubigeo'
    id_ubigeo = db.Column(db.Integer, primary_key=True) 
    latitud = db.Column(db.Integer)
    longitud = db.Column(db.Integer)

    def __init__(self, id_ubigeo, latitud, longitud):
        self.id_ubigeo = id_ubigeo
        self.latitud = latitud
        self.longitud = longitud