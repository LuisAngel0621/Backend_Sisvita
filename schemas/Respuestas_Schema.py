from ma import ma
from models.Respuestas import respuestasModel

class RespuestaSchema(ma.Schema):
    class Meta:
        model = respuestasModel
        fields = (
                  'id_respuestas',
                  'descripcion'
                  )
Tests_Schema = RespuestaSchema(many=True)
Test_Schema = RespuestaSchema()