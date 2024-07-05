from ma import ma
from models.Diagnostico import Diagnostico
from schemas.UsuarioTest_schema import UsuarioTestSchema
from schemas.Nivel_Schema import NivelSchema

class DiagnosticoSchema(ma.Schema):
    class Meta:
        model = Diagnostico
        fields = ('id_diag',
                  'id_user_test',
                  'puntaje',
                  'comentario',
                  'recomendacion',
                  'notificacion',
                  'usuario_test',
                  'tipo_nivel'
                  )
    usuario_test = ma.Nested(UsuarioTestSchema, only =('fecha_test','usuario_tipo','test'))
    tipo_nivel = ma.Nested(NivelSchema, only = ('nivel_ansiedad',))
Diagnosticos_Schema = DiagnosticoSchema(many=True)
Diagnostico_Schema = DiagnosticoSchema()
