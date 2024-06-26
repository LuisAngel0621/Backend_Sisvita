from ma import ma
from models.Preguntas import Preguntas

class PreguntaSchema(ma.Schema):
    class Meta:
        model = Preguntas
        fields = (
                  'id_preguntas',
                  'descripcion'
                  )
Preguntas_Schema = PreguntaSchema(many=True)
Pregunta_Schema = PreguntaSchema()