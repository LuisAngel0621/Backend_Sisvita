from db import db

class Usuario(db.Model):
    __tablename__ = 'tb_usuario'
    id_usu = db.Column(db.Integer, primary_key=True)
    id_ubigeo = db.Column(db.Integer, db.ForeignKey('tb_ubigeo.id_ubigeo'))
    nombres = db.Column(db.String)
    apellidos = db.Column(db.String)
    correoinstitucional = db.Column(db.String)
    edad = db.Column(db.Integer)
    sexo = db.Column(db.String)
    estadocivil = db.Column(db.String)
    ocupacion = db.Column(db.String)
    ubigeo = db.relationship('Ubigeo', backref='tb_usuario')

    def __init__(self, nombres, apellidos, correoinstitucional, edad, sexo, estadocivil, ocupacion):
        self.nombres = nombres
        self.apellidos = apellidos
        self.correoinstitucional = correoinstitucional
        self.edad = edad
        self.sexo = sexo
        self.estadocivil = estadocivil
        self.ocupacion = ocupacion