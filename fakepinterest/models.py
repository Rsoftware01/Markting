# criar o modelo do banco de dados

from fakepinterest import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get (int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    telefone = database.Column(database.String, nullable=False)
    infos = database.relationship("Info", backref="usuario", lazy=True)  # Relacionamento com a classe Info
    outras_infos = database.relationship("OutraInfo", backref="usuario", lazy=True)  # Relacionamento com a classe OutraInfo

class Info(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    objetivoimediato = database.Column(database.String, nullable=False)
    objetivo3a5anos = database.Column(database.String, nullable=False)
    objetivo5a10anos = database.Column(database.String, nullable=False)
    usuario_id = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)  # Chave estrangeira

class OutraInfo(database.Model):  # Renomeando para evitar conflito
    id = database.Column(database.Integer, primary_key=True)
    idadehoje = database.Column(database.Integer, nullable=False)  # Corrigido para database.Integer
    valorinvestido = database.Column(database.Float, nullable=False)  # Corrigido para database.Float
    pouparmes = database.Column(database.Float, nullable=False)  # Corrigido para database.Float
    idadeaposentar = database.Column(database.Integer, nullable=False)  # Corrigido para database.Integer
    rendaaposentar = database.Column(database.Float, nullable=False)  # Corrigido para database.Float
    risco = database.Column(database.Integer, nullable=False)  # Corrigido para database.Integer
    usuario_id = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)  # Chave estrangeira
