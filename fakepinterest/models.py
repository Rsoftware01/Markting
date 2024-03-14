# criar o modelo do banco de dados
#aqui é as colunas do formul

from fakepinterest import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

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
    idadehoje = database.Column(database.Float, nullable=False)
    valorinvestido = database.Column(database.Float, nullable=False)
    pouparmes = database.Column(database.Float, nullable=False)
    idadeaposentar = database.Column(database.Float, nullable=False)
    rendaaposentar = database.Column(database.Float, nullable=False)
    expectativavida = database.Column(database.Float, nullable=False)
    risco = database.Column(database.String, nullable=False)

    def idadehoje_formatted(self):
        return str(self.idadehoje).rstrip('0').rstrip('.') if '.' in str(self.idadehoje) else str(self.idadehoje)

    def valorinvestido_formatted(self):
        return str(self.valorinvestido).rstrip('0').rstrip('.') if '.' in str(self.valorinvestido) else str(self.valorinvestido)

    def pouparmes_formatted(self):
        return str(self.pouparmes).rstrip('0').rstrip('.') if '.' in str(self.pouparmes) else str(self.pouparmes)

    def idadeaposentar_formatted(self):
        return str(self.idadeaposentar).rstrip('0').rstrip('.') if '.' in str(self.idadeaposentar) else str(self.idadeaposentar)

    def rendaaposentar_formatted(self):
        return str(self.rendaaposentar).rstrip('0').rstrip('.') if '.' in str(self.rendaaposentar) else str(self.rendaaposentar)

    def expectativavida_formatted(self):
        return str(self.expectativavida).rstrip('0').rstrip('.') if '.' in str(self.expectativavida) else str(self.expectativavida)


    #idadehojee = database.Column(database.String, nullable=False)
    #Tempo_contribuicao = database.Column(database.String, nullable=False)
    #valoraposentarrr = database.Column(database.String, nullable=False)
    #Tempo_beneficio = database.Column(database.String, nullable=False)
    #volume_precisa_acumular = database.Column(database.String, nullable=False)
    #Valor_que_deve_juntar_anualmente = database.Column(database.String, nullable=False)
   # Valor_que_deve_juntar_mensalmente = database.Column(database.String, nullable=False)
