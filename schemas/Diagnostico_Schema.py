from ma import ma
from models.Diagnostico import Diagnostico

class DiagnosticoSchema(ma.Schema):
    class Meta:
        model = Diagnostico
        fields = (
                  'id_diag',
                  'id_usutip',
                  'nombres',
                  'apellidos',
                  'tipo_test',
                  'id_nivel',
                  'puntaje',
                  'comentario',
                  'recomendacion',
                  'notificacion',
                  'fecha_test'
                  )
Diagnosticos_Schema = DiagnosticoSchema(many=True)
Diagnostico_Schema = DiagnosticoSchema()
