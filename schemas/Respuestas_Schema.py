from ma import ma
from models.Respuestas import Respuestas

class RespuestaSchema(ma.Schema):
    class Meta:
        model = Respuestas
        fields = (
                  'id_respuestas',
                  'descripcion'
                  )
Respuestas_Schema = RespuestaSchema(many=True)
Respuesta_Schema = RespuestaSchema()