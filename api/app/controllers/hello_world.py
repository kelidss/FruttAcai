from flask import Blueprint

# blueprint para o controller de teste
hello_world_bp = Blueprint('hello_world', __name__)

@hello_world_bp.route('/hello_world', methods=['GET'])
def hello_world_route():
    return {"message": "Olá, mundo!"}, 200
