from ma import ma
from models.Nivel import Nivel

class NivelSchema(ma.Schema):
    class Meta:
        model = Nivel
        fields = (
                  'id_nivel',
                  'rang_min',
                  'rang_max',
                  'nivel_ansiedad'
                  )
Niveles_Schema = NivelSchema(many=True)
Nivel_Schema = NivelSchema()