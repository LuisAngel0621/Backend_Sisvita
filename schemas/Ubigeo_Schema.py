from ma import ma
from models.Ubigeo import Ubigeo

class UbigeoSchema(ma.Schema):
    class Meta:
        model = Ubigeo
        fields = (
                  'id_ubigeo',
                  'id_usu',
                  'latitud',
                  'longitud',
                  'nivel_ansiedad',
                  'fecha'
                  )
Ubigeos_Schema = UbigeoSchema(many=True)
Ubigeo_Schema = UbigeoSchema()