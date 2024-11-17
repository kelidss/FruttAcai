from app.models.user import User
from app import db

def create_user(data):
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return user
