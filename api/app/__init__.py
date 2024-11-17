from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .controllers import register_blueprints

# inicializa o banco de dados
print("Iniciou o banco")
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # inicializa as extensoes
    db.init_app(app)

    # registra rotas automaticamente
    register_blueprints(app)

    with app.app_context():
        try:
            from . import models
            db.create_all()  # cria as tabelas apenas se elas nao existirem
            print("Tabelas criadas com sucesso.")
        except Exception as e:
            print(f"Erro ao criar tabelas: {e}")

    return app
