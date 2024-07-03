from ma import ma
from models.UsuarioTipo import UsuarioTipo
from schemas.Usuario_schema import UsuarioSchema

class UsuarioTipoSchema(ma.Schema):
    class Meta:
        model = UsuarioTipo
        fields = ('id_usutip',
                  'id_tipo',
                  'id_usu',
                  'sesion',
                  'fechasesion',
                  'contrasenia',
                  'condiciones',
                  'terminos',
                  'contraseñahash',
                  'usuario')
    usuario = ma.Nested(UsuarioSchema, only = ('nombres','apellidos'))

Usuario_Tipo_Schema = UsuarioTipoSchema(only = ["id_usutip",])