from ma import ma
from models.Categoria import Categoria

class CategoriaSchema(ma.Schema):
    class Meta:
        model = Categoria
        fields = (
                  'id_categoria',
                  'nombre'
                  )
Categorias_Schema = CategoriaSchema(many=True)
Categoria_Schema = CategoriaSchema()