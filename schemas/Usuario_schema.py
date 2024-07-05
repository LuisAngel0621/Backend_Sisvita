from ma import ma
from models.Usuario import Usuario
from schemas.Ubigeo_Schema import UbigeoSchema

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
                  'ocupacion',
                  'ubigeo')
        
    ubigeo = ma.Nested(UbigeoSchema, only=('latitud','longitud'))
Usuario_Schema = UsuarioSchema()