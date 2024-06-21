from ma import ma
from models.Diagnostico import Diagnostico

class DiagnosticoSchema(ma.Schema):
    class Meta:
        model = Diagnostico
        fields = (
                  'id_diag',
                  'id_user_test',
                  'sum_cognitivo',
                  'sum_fisiologico',
                  'sum_motor',
                  'diagnostico'
                  )
Diagnosticos_Schema = DiagnosticoSchema(many=True)
Diagnostico_Schema = DiagnosticoSchema()