from ma import ma
from models.Test import Test

class TestSchema():
    class Meta:
        model = Test
        fields = ('id_test',
                  'id_dialog',
                  'id_cat',
                  'fechatnoma',
                  'estado')
    

Test_Schema = TestSchema()