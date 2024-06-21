from db import db

class Diagnostico(db.Model):
    __tablename__ = 'tb_diagnostico'
    id_diag = db.Column(db.Integer, primary_key=True) 
    id_user_test = db.Column(db.Integer)
    sum_cognitivo = db.Column(db.Integer)
    sum_fisiologico = db.Column(db.Integer)
    sum_motor = db.Column(db.Integer)
    diagnostico = db.Column(db.String)

    def __init__(self, id_diag, id_user_test, sum_cognitivo, sum_fisiologico, sum_motor, diagnostico):
        self.id_diag = id_diag
        self.id_user_test = id_user_test
        self.sum_cognitivo = sum_cognitivo
        self.sum_fisiologico = sum_fisiologico
        self.sum_motor = sum_motor
        self.diagnostico = diagnostico