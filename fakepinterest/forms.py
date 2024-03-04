from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, Optional, ValidationError
from fakepinterest.models import Usuario

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, Optional

class FormPagina1(FlaskForm):
    nome = StringField('Nome: ', validators=[DataRequired()])
    telefone = StringField('Telefone para envio dos Resultados: ', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    indicou = RadioField('Quem te indicou:',
                         choices=[('Assessor(a)', 'Assessor(a)'),
                                  ('Redes sociais', 'Redes sociais'),
                                  ('Outras', 'Outras')],
                         validators=[DataRequired()])
    outras_indicacoes = StringField('Outras indicações:', validators=[Optional()])
    submit = SubmitField('Próxima Página')

class FormPagina2(FlaskForm):
    objetivo_imediato = RadioField('Qual é o seu objetivo financeiro mais imediato?',
                                   choices=[('viagem', 'Economizar para uma viagem'),
                                            ('emergencia', 'Montar uma reserva de emergência'),
                                            ('dividas', 'Pagar dívidas'),
                                            ('outras_imediatas', 'Outras')],
                                   validators=[DataRequired()])
    objetivo_imediato_outras = StringField('Por favor, especifique:', validators=[Optional()])
    objetivo_3a5_anos = RadioField('Qual é o seu objetivo financeiro para os próximos 3 a 5 anos?',
                                   choices=[('carro', 'Comprar um carro novo'),
                                            ('educacao', 'Fazer um curso ou investir em educação'),
                                            ('casa', 'Economizar para uma entrada de casa'),
                                            ('outras_3a5', 'Outras')],
                                   validators=[DataRequired()])
    objetivo_3a5_anos_outras = StringField('Por favor, especifique:', validators=[Optional()])
    objetivo_5a10_anos = RadioField('Qual é o seu objetivo financeiro para os próximos 5 a 10 anos?',
                                    choices=[('casa_propria', 'Adquirir uma casa própria'),
                                             ('negocio', 'Investir em um negócio próprio'),
                                             ('educacao_filhos', 'Planejar a educação dos filhos'),
                                             ('outras_5a10', 'Outras')])
    objetivo_5a10_anos_outras = StringField('Por favor, especifique:', validators=[Optional()])
    submit = SubmitField('Próxima Página')

class FormPagina3(FlaskForm):
    idade_hoje = FloatField('Qual a sua idade hoje?', validators=[DataRequired()])
    valor_investido = FloatField('Você já possui algum valor investido, qual?', validators=[DataRequired()])
    poupar_mes = FloatField('Quanto conseguiria poupar por mês?', validators=[DataRequired()])
    idade_aposentar = FloatField('Qual idade você pretende se aposentar?', validators=[DataRequired()])
    renda_aposentar = FloatField('Qual renda você gostaria para a sua aposentadoria?', validators=[DataRequired()])
    tolerancia_risco = RadioField('Qual é o seu nível de tolerância ao risco quando se trata de investimentos?',
                                  choices=[('conservador', 'Conservador: Prefiro opções de investimento de baixo risco, mesmo que isso signifique retornos mais baixos. (IPCA+5%)'),
                                           ('moderado', 'Moderado: Estou disposto(a) a assumir algum risco em busca de retornos moderados. (IPCA+7%)'),
                                           ('agressivo', 'Agressivo: Estou disposto(a) a assumir riscos significativos em busca de retornos mais altos. (IPCA+10%)')],
                                  validators=[DataRequired()])


    submit = SubmitField('Enviar')


    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Email já cadastrado. Preencha com outro.")
