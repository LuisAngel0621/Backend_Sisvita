from ma import ma
from models.TipoTest import TipoTest

class TipoTestSchema(ma.Schema):
    class Meta:
        model = TipoTest
        fields = ('id_tipotest',
                  'nombre',
                  'cantpregunta')
    
Tipo_Tests_Schema = TipoTestSchema( many = True)
Tipo_Test_Schema = TipoTestSchema()