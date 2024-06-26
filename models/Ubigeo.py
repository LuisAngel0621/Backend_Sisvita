from db import db

class Ubigeo(db.Model):
    __tablename__ = 'tb_ubigeo'
    id_ubigeo = db.Column(db.Integer, primary_key=True) 
    id_usu = db.Column(db.Integer, db.ForeignKey('tb_usuario.id_usu'))
    latitud = db.Column(db.Integer)
    longitud = db.Column(db.Integer)
    nivel_ansiedad = db.Column(db.String)
    fecha = db.Column(db.Date)

    def __init__(self, id_ubigeo, id_usu, latitud, longitud, nivel_ansiedad, fecha):
        self.id_ubigeo = id_ubigeo
        self.id_usu = id_usu
        self.latitud = latitud
        self.longitud = longitud
        self.nivel_ansiedad = nivel_ansiedad
        self.fecha = fecha