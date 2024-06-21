from ma import ma
from models.Usuario import Usuario

class UsuarioSchema(ma.Schema):
    class Meta:
        model = Usuario
        fields = ('id_usu',
                  'nombres',
                  'apellidos',
                  'correoinstitucional',
                  'edad',
                  'sexo',
                  'estadocivil',
                  'ocupacion')

Usuario_Schema = UsuarioSchema()