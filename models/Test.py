from db import db

class Test(db.Model):
    __tablename__ = 'tb_test'
    id_test = db.Column(db.Integer, primary_key=True)
    id_tipotest = db.Column(db.Integer, db.ForeignKey('tb_tipotest.id_tipotest'))
    estado = db.Column(db.Boolean)
    id_categoria = db.Column(db.Integer, db.ForeignKey('tb_categoria.id_categoria'))
    tipo_test = db.relationship('TipoTest', backref='tb_test')

    def __init__(self, id_test, id_cat, estado, id_categoria):
        self.id_test = id_test
        self.id_cat = id_cat
        self.estado = estado
        self.id_categoria = id_categoria