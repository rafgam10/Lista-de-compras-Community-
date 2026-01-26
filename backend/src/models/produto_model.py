from src.settings.extersions import db

class Produto(db.Model):
    
    __tablename__ = "produtos"
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    nome = db.Column(db.String, nullable=False, index=True)
    status = db.Column(db.Boolean, nullable=False, default=True, index=True)
    
    def __init__(self, nome, status):
        self.nome = nome
        self.status = status
    
    def __repr(self):
        return f"Produto: {self.id}.{self.nome} - {self.status}"