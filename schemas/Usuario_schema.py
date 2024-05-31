from ma import ma
from models.Usuario import Usuario

class UsuarioSchema():
    class Meta:
        model = Usuario
        fields = ('id_usu',
                  'nombres',
                  'apellidos',
                  'correoconst',
                  'edad',
                  'sexo',
                  'estadocivil',
                  'ocupacion')

Usuario_Schema = UsuarioSchema()