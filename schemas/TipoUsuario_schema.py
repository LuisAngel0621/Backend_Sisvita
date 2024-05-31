from ma import ma
from models.TipoUsuario import TipoUsuario

class TipoUsuarioSchema():
    class Meta:
        model = TipoUsuario
        fields = ('id_tipo',
                  'tipo',
                  'estado')
    

Tipo_Usuario_Schema = TipoUsuarioSchema()