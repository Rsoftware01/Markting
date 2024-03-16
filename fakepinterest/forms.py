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
    indicou = RadioField('Como nos conheceu:',
                         choices=[('Assessor(a)', 'Assessor(a)'),
                                  ('Indicação', 'Indicação'),
                                  ('Redes_sociais', 'Redes sociais'),
                                  ('Pesquisa_Google', 'Pesquisa no Google')],
                         validators=[DataRequired()])
    outras_indicacoes1 = StringField('Se foi através dos nossos assessores, escreva o nome por favor:',
        validators=[Optional()])
    submit = SubmitField('Próxima Página')

class FormPagina2(FlaskForm):
    objetivo_imediato = RadioField('Qual é o seu objetivo financeiro mais imediato?',
                                   choices=[('Viagem', 'Economizar para uma viagem'),
                                            ('Emergência', 'Montar uma reserva de emergência'),
                                            ('Dívidas', 'Pagar dívidas'),
                                            ('Outros', 'Outras')],
                                   validators=[DataRequired()])
    objetivo_imediato_outras = StringField('Por favor, especifique:', validators=[Optional()])
    objetivo_3a5_anos = RadioField('Qual é o seu objetivo financeiro para os próximos 3 a 5 anos?',
                                   choices=[('Carro', 'Comprar um carro novo'),
                                            ('Educação', 'Fazer um curso ou investir em educação'),
                                            ('Casa', 'Economizar para uma entrada de casa'),
                                            ('Outros', 'Outras')],
                                   validators=[DataRequired()])
    objetivo_3a5_anos_outras = StringField('Por favor, especifique:', validators=[Optional()])
    objetivo_5a10_anos = RadioField('Qual é o seu objetivo financeiro para os próximos 5 a 10 anos?',
                                    choices=[('Casa_propria', 'Adquirir uma casa própria'),
                                             ('Negocio', 'Investir em um negócio próprio'),
                                             ('eEducação_filhos', 'Planejar a educação dos filhos'),
                                             ('Outros', 'Outras')])
    objetivo_5a10_anos_outras = StringField('Por favor, especifique:', validators=[Optional()])
    submit = SubmitField('Próxima Página')

class FormPagina3(FlaskForm):
    idade_hoje = FloatField('Qual a sua idade hoje?', validators=[DataRequired()])
    valor_investido = FloatField('Quanto você possui investido até o momento?', validators=[DataRequired()])
    poupar_mes = FloatField('Quanto conseguiria poupar por mês?', validators=[DataRequired()])
    idade_aposentar = FloatField('Qual idade você pretende se aposentar?', validators=[DataRequired()])
    renda_aposentar = FloatField('Qual renda mensal você gostaria de ter na sua aposentadoria?', validators=[DataRequired()])
    expectativavida = FloatField('Qual a sua expectativa de vida?', validators=[DataRequired()])
    tolerancia_risco = RadioField('Qual é o seu nível de tolerância ao risco quando se trata de investimentos?',
                                  choices=[('conservador', 'Conservador: Prefiro opções de investimento de baixo risco, mesmo que isso signifique retornos mais baixos - (IPCA+5%).'),
                                           ('moderado', 'Moderado: Estou disposto(a) a assumir algum risco em busca de retornos moderados - (IPCA+7%).'),
                                           ('agressivo', 'Agressivo: Estou disposto(a) a assumir riscos significativos em busca de retornos mais altos - (IPCA+10%).')],
                                  validators=[DataRequired()])


    submit = SubmitField('Enviar')


    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Email já cadastrado. Preencha com outro.")