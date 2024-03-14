# criar o modelo do banco de dados
#aqui é as colunas do formul

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
    indicou = database.Column(database.String, nullable=False)
    outras_indicacoes1 = database.Column(database.String, nullable=False)
    objetivoimediato = database.Column(database.String, nullable=False)
    objetivo_imediato_outras = database.Column(database.String, nullable=False)
    objetivo3a5anos = database.Column(database.String, nullable=False)
    objetivo_3a5_anos_outras = database.Column(database.String, nullable=False)
    objetivo5a10anos = database.Column(database.String, nullable=False)
    objetivo_5a10_anos_outras = database.Column(database.String, nullable=False)
    idadehoje = database.Column(database.Float, nullable=False)  # Alterado para database.Float
    valorinvestido = database.Column(database.String, nullable=False)
    pouparmes = database.Column(database.String, nullable=False)
    idadeaposentar = database.Column(database.String, nullable=False)
    rendaaposentar = database.Column(database.String, nullable=False)
    expectativavida = database.Column(database.String, nullable=False)
    risco = database.Column(database.String, nullable=False)

    #idadehojee = database.Column(database.String, nullable=False)
    #Tempo_contribuicao = database.Column(database.String, nullable=False)
    #valoraposentarrr = database.Column(database.String, nullable=False)
    #Tempo_beneficio = database.Column(database.String, nullable=False)
    #volume_precisa_acumular = database.Column(database.String, nullable=False)
    #Valor_que_deve_juntar_anualmente = database.Column(database.String, nullable=False)
   # Valor_que_deve_juntar_mensalmente = database.Column(database.String, nullable=False)
