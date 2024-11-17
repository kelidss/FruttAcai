from app import db
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True  # define como abstrato para nao criar tabela no banco

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
