from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from Config import Config

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from routes import todo_bp
        app.register_blueprint(todo_bp, url_prefix='/api')

        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)