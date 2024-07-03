from ma import ma
from models.Test import Test
from schemas.TipoTest_Schema import TipoTestSchema

class TestSchema(ma.Schema):
    class Meta:
        model = Test
        fields = ('id_test',
                  'id_cat',
                  'fechatnoma',
                  'estado',
                  'tipo_test')
    tipo_test = ma.Nested(TipoTestSchema, only = ('nombre',))
Test_Schema = TestSchema()