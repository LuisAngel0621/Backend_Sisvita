from ma import ma
from models.UsuarioTest import UsuarioTest

class UsuarioTestSchema():
    class Meta:
        model = UsuarioTest
        fields = ('id_user_test',
                  'id_test',
                  'id_paciente',
                  'pregunta',
                  'respuesta',
                  'nropregunta')
Usuario_Test_Schema = UsuarioTestSchema()