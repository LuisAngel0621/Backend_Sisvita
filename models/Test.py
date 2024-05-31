from db import db

class Test(db.Model):
    __tablename__ = 'tb_test'
    id_test = db.Column(db.Integer, primary_key=True) 
    id_dialog = db.Column(db.Integer)
    id_cat = db.Column(db.Integer)
    fechatnoma = db.Column(db.Date)
    estado = db.Column(db.Boolean)

    def __init__(self, id_test, id_dialog, id_cat, fechatnoma, estado):
        self.id_test = id_test
        self.id_dialog = id_dialog
        self.id_cat = id_cat
        self.fechatnoma = fechatnoma
        self.estado = estado