from ma import ma
from models.UsuarioTipo import UsuarioTipo

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
                  'contraseñahash')

Usuario_Tipo_Schema = UsuarioTipoSchema()