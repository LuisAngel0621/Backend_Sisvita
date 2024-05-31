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
    contrasenia = db.Column(db.String)
    condiciones = db.Column(db.Boolean)
    terminos = db.Column(db.Boolean)


    def __init__(self, id_tipo, tipo, estado):
        self.id_tipo = id_tipo
        self.tipo = tipo
        self.estado = estado