from db import db
from models.TipoUsuario import TipoUsuario
from models.Usuario import Usuario

class UsuarioTipo(db.Model):
    __tablename__ = 'tb_usuario_tipo'
    id_usutip = db.Column(db.Integer, primary_key=True) 
    id_tipo = db.Column(db.Integer, db.ForeignKey('tb_tipousuario.id_tipo'))
    id_usu = db.Column(db.Integer, db.ForeignKey('tb_usuario.id_usu'))
    sesion = db.Column(db.Boolean)
    fechasesion = db.Column(db.Date)
    contraseña = db.Column(db.String)
    condiciones = db.Column(db.Boolean)
    terminos = db.Column(db.Boolean)
    contraseñahash = db.Column(db.String)


    def __init__(self, id_tipo, id_usu, sesion,fechasesion,contraseña,condiciones,terminos,contraseñahash):
        self.id_tipo = id_tipo
        self.id_usu = id_usu
        self.sesion = sesion
        self.fechasesion = fechasesion
        self.contraseña = contraseña
        self.condiciones = condiciones
        self.terminos = terminos
        self.contraseñahash = contraseñahash
