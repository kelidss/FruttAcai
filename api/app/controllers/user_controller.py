from flask import Blueprint, jsonify, request
from app.models.user import User
from app import db
from app.services import user_service

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([
        {
            'id': user.id,
            'name': user.name,
            'email': user.email
        } for user in users
    ])

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_service.create_user(data)
    return jsonify({
        'message': 'User created'
    }), 201
