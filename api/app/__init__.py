from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Inicializa o banco de dados
print("Iniciou o banco")
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa as extensões
    db.init_app(app)

    # Registra rotas
    from .controllers import api_bp
    app.register_blueprint(api_bp)

    # Importa os modelos
    with app.app_context():
        from app import models
        db.create_all()  # Cria as tabelas no banco de dados

    return app
