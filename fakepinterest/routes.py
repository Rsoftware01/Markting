import pdfkit
from flask import render_template, redirect, url_for, flash, session
from flask import redirect, url_for, request, flash
from fakepinterest import app, database
from fakepinterest.models import Usuario
from flask_login import login_required
from fakepinterest.forms import FormPagina1, FormPagina2, FormPagina3
from math import pow
from babel.numbers import format_currency

@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormPagina1()
    if formlogin.validate_on_submit():
        session['nome'] = formlogin.nome.data
        session['telefone'] = formlogin.telefone.data
        session['email'] = formlogin.email.data
        session['indicou'] = formlogin.indicou.data
        session['outras_indicacoes1'] = formlogin.outras_indicacoes1.data
        return redirect(url_for('info2'))  # Redireciona para a próxima página após o envio
    return render_template("homepage.html", form=formlogin)

@app.route("/info2", methods=["GET", "POST"])
def info2():
    form2 = FormPagina2()
    if form2.validate_on_submit():
        session['objetivo_imediato'] = form2.objetivo_imediato.data
        session['objetivo_imediato_outras'] = form2.objetivo_imediato_outras.data
        session['objetivo_3a5_anos'] = form2.objetivo_3a5_anos.data
        session['objetivo_3a5_anos_outras'] = form2.objetivo_3a5_anos_outras.data
        session['objetivo_5a10_anos'] = form2.objetivo_5a10_anos.data
        session['objetivo_5a10_anos_outras'] = form2.objetivo_5a10_anos_outras.data
        return redirect(url_for('info3'))  # Redireciona para a próxima página após o envio
    return render_template("info2.html", form=form2)

@app.route("/info3", methods=["GET", "POST"])
def info3():
    form3 = FormPagina3()
    if form3.validate_on_submit():
        # Salva os dados do formulário no banco de dados
        usuario = Usuario(
            nome=session['nome'],
            telefone=session['telefone'],
            email=session['email'],
            indicou=session['indicou'],
            outras_indicacoes1=session['outras_indicacoes1'],
            objetivoimediato=session['objetivo_imediato'],
            objetivo_imediato_outras=session['objetivo_imediato_outras'],
            objetivo3a5anos=session['objetivo_3a5_anos'],
            objetivo_3a5_anos_outras=session['objetivo_3a5_anos_outras'],
            objetivo5a10anos=session['objetivo_5a10_anos'],
            objetivo_5a10_anos_outras=session['objetivo_5a10_anos_outras'],
            idadehoje=form3.idade_hoje.data,
            valorinvestido=form3.valor_investido.data,
            pouparmes=form3.poupar_mes.data,
            idadeaposentar=form3.idade_aposentar.data,
            rendaaposentar=form3.renda_aposentar.data,
            expectativavida=form3.expectativavida.data,
            risco=form3.tolerancia_risco.data
        )
        database.session.add(usuario)
        database.session.commit()
        # Redireciona para a página de resultados após o envio
        return redirect(url_for('resultados'))
    return render_template("info3.html", form=form3)


@app.route("/resultados", methods=["GET", "POST"])
def resultados():
    ultima_info = Usuario.query.order_by(Usuario.id.desc()).first()

    # Obtendo as informações do objeto e convertendo para os tipos corretos
    idadehoje = float(ultima_info.idadehoje)
    idadeaposentar = float(ultima_info.idadeaposentar)
    rendaaposentar = float(ultima_info.rendaaposentar)
    valorinvestido = float(ultima_info.valorinvestido)
    expectativavida = float(ultima_info.expectativavida)

    # Calculando as métricas com base nos dados capturados
    Tempo_contribuicao = int(idadeaposentar - idadehoje)
    Tempo_beneficio = int(expectativavida - idadeaposentar)
    idadehoje = int(idadehoje)
    idadeaposentar = int(idadeaposentar)

    # Dados fictícios para demonstração
    taxa = 0.05  # 5%
    inflacao = 0.03  # 3%

    Renda_corrigida_inflacao = rendaaposentar * pow(1 + inflacao, Tempo_contribuicao)

    Renda_anual_corrigida_inflacao = abs(Renda_corrigida_inflacao * 12)

    Valor_necessario_inicio_aposentadoria = Renda_anual_corrigida_inflacao * ((1 - pow(1 + taxa, -Tempo_beneficio)) / taxa)

    Valor_ativos_corrigidos_ate_aposentadoria = valorinvestido * pow(1 + taxa, Tempo_contribuicao)

    volume_precisa_acumular = abs(Valor_necessario_inicio_aposentadoria - Valor_ativos_corrigidos_ate_aposentadoria)

    Valor_que_deve_juntar_anualmente = (-volume_precisa_acumular * taxa) / (1 - pow(1 + taxa, Tempo_contribuicao))

    Valor_que_deve_juntar_mensalmente = volume_precisa_acumular / (
                ((pow(taxa + 1, 1 / 12)) ** (Tempo_contribuicao * 12) - 1) / (taxa / 12))

    # Formata os valores para exibição no formato de moeda brasileira
    valoraposentarr = format_currency(valorinvestido, 'BRL', locale='pt_BR')
    rendaaposentarr = format_currency(rendaaposentar, 'BRL', locale='pt_BR')
    Renda_anual_corrigida_inflacao = format_currency(Renda_anual_corrigida_inflacao, 'BRL', locale='pt_BR')
    Valor_necessario_inicio_aposentadoria = format_currency(Valor_necessario_inicio_aposentadoria, 'BRL', locale='pt_BR')
    Valor_ativos_corrigidos_ate_aposentadoria = format_currency(Valor_ativos_corrigidos_ate_aposentadoria, 'BRL', locale='pt_BR')
    volume_precisa_acumular = format_currency(volume_precisa_acumular, 'BRL', locale='pt_BR')
    Valor_que_deve_juntar_anualmente = format_currency(Valor_que_deve_juntar_anualmente, 'BRL', locale='pt_BR')
    Valor_que_deve_juntar_mensalmente = format_currency(Valor_que_deve_juntar_mensalmente, 'BRL', locale='pt_BR')

    return render_template("resultados.html",
                           Tempo_contribuicao=Tempo_contribuicao,
                           idadehojee=idadehoje,
                           idadeaposentarr=idadeaposentar,
                           rendaaposentarrr=rendaaposentarr,
                           Tempo_beneficio=Tempo_beneficio,
                           Renda_anual_corrigida_inflacao=Renda_anual_corrigida_inflacao,
                           valoraposentarrr=valoraposentarr,
                           Valor_necessario_inicio_aposentadoria=Valor_necessario_inicio_aposentadoria,
                           Valor_ativos_corrigidos_ate_aposentadoria=Valor_ativos_corrigidos_ate_aposentadoria,
                           volume_precisa_acumular=volume_precisa_acumular,
                           Valor_que_deve_juntar_anualmente=Valor_que_deve_juntar_anualmente,
                           Valor_que_deve_juntar_mensalmente=Valor_que_deve_juntar_mensalmente)
