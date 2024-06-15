from db import db

class Test(db.Model):
    __tablename__ = 'tb_test'
    id_test = db.Column(db.Integer, primary_key=True) 
    id_dialog = db.Column(db.Integer)
    id_tipotest = db.Column(db.Integer, db.ForeignKey('tb_tipotest.id_tipotest'))
    fechatnoma = db.Column(db.Date)
    estado = db.Column(db.Boolean)
    id_categoria = db.Column(db.Integer, db.ForeignKey('tb_categoria.id_categoria'))

    def __init__(self, id_test, id_dialog, id_cat, fechatnoma, estado, id_categoria):
        self.id_test = id_test
        self.id_dialog = id_dialog
        self.id_cat = id_cat
        self.fechatnoma = fechatnoma
        self.estado = estado
        self.id_categoria = id_categoria