from ma import ma
from models.Preguntas import preguntaModel

class PreguntaSchema(ma.Schema):
    class Meta:
        model = preguntaModel
        fields = (
                  'id_preguntas',
                  'descripcion'
                  )
Tests_Schema = PreguntaSchema(many=True)
Test_Schema = PreguntaSchema()