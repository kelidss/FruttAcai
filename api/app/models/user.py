from app.models.base_model import BaseModel
from app import db

class User(BaseModel):
    __tablename__ = 'users'
    
    name = db.Column(db.String(100), unique=False, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    type_user = db.Column(db.String(20), nullable=False, default="cliente")

    def __repr__(self):
        return f'<User {self.name}>'
