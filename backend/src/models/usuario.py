# backend/src/model/user.py
from backend.src.extensions import db # Importa o objeto db do seu app.py

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'