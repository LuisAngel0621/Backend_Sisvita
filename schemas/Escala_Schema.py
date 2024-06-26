from ma import ma
from models.Escala import Escala

class EscalaSchema(ma.Schema):
    class Meta:
        model = Escala
        fields = (
                  'id_escala',
                  'descripcion'
                  )
Escalas_Schema = EscalaSchema(many=True)
Escala_Schema = EscalaSchema()