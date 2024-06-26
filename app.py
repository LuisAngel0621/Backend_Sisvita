from flask import Flask
from routes.RegistrarUsuario import usuario
from routes.RealizarTest import respuestas
from routes.IniciarSesion import sesion
from routes.RealizarVigilancia import vigilancia
from routes.VisualizarMapaCalor import mapacalor
from routes.EvaluarTest import evaluar
from Config import DATABASE_CONNECTION_URI
from flask_cors import CORS
from db import db
from ma import ma


app = Flask(__name__)
        
CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app, supports_credentials=True)
app.secret_key = 'clavesecreta123'

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db.init_app(app)
ma.init_app(app)
app.register_blueprint(usuario)
app.register_blueprint(respuestas)
app.register_blueprint(sesion)
app.register_blueprint(vigilancia)
app.register_blueprint(mapacalor)
app.register_blueprint(evaluar)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")