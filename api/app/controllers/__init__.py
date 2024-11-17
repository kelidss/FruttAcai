import glob
import os
from flask import Blueprint

# Função para registrar todos os Blueprints
def register_blueprints(app):
    # Caminho para todos os arquivos Python na pasta controllers
    controllers_path = os.path.join(os.path.dirname(__file__), "*.py")

    # Loop para importar todos os controladores
    for controller_file in glob.glob(controllers_path):
        # Ignora o próprio __init__.py
        if "__init__.py" in controller_file:
            continue
        
        # Importa o controlador
        module_name = os.path.basename(controller_file)[:-3]  # Remove ".py"
        module = __import__(f"app.controllers.{module_name}", fromlist=[module_name])
        
        # Registra todos os Blueprints encontrados
        for blueprint in module.__dict__.values():
            if isinstance(blueprint, Blueprint):
                app.register_blueprint(blueprint)
