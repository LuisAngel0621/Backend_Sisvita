from ma import ma
from models.UsuarioTest import UsuarioTest
from schemas.UsuarioTipo_schema import UsuarioTipoSchema
from schemas.Test_schema import TestSchema

class UsuarioTestSchema(ma.Schema):
    class Meta:
        model = UsuarioTest
        fields = ('id_user_test',
                  'id_test',
                  'id_paciente',
                  'id_escala',
                  'id_respuestas',
                  'id_preguntas',
                  'usuario_tipo',
                  'test')
    usuario_tipo = ma.Nested(UsuarioTipoSchema, only=('usuario',))
    test = ma.Nested(TestSchema, only =('tipo_test',))
Usuario_Test_Schema = UsuarioTestSchema()