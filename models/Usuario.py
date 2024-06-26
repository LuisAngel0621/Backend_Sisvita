from db import db

class Usuario(db.Model):
    __tablename__ = 'tb_usuario'
    id_usu = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String)
    apellidos = db.Column(db.String)
    correoinstitucional = db.Column(db.String)
    edad = db.Column(db.Integer)
    sexo = db.Column(db.String)
    estadocivil = db.Column(db.String)
    ocupacion = db.Column(db.String)

    def __init__(self, nombres, apellidos, correoinstitucional, edad, sexo, estadocivil, ocupacion):
        self.nombres = nombres
        self.apellidos = apellidos
        self.correoinstitucional = correoinstitucional
        self.edad = edad
        self.sexo = sexo
        self.estadocivil = estadocivil
        self.ocupacion = ocupacion