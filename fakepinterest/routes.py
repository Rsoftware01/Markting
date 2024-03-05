# criar as rotas do site, os links

from flask import render_template, redirect, url_for, request, flash
from fakepinterest import app, database
from fakepinterest.models import Usuario, Info, OutraInfo
from flask_login import login_required
from fakepinterest.forms import FormPagina1, FormPagina2, FormPagina3

@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormPagina1()
    if formlogin.validate_on_submit():
        # Verifica se o e-mail já está cadastrado
        usuario_existente = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario_existente:
            flash('E-mail já cadastrado. Por favor, use um e-mail diferente.')
            return redirect(url_for('homepage'))
        else:
            # Se o e-mail não estiver cadastrado, prossegue com o cadastro
            usuarioo = Usuario(nome=formlogin.nome.data,
                              telefone=formlogin.telefone.data,
                              email=formlogin.email.data,
                              indicou=formlogin.indicou.data,
                              outras_indicacoes1=formlogin.indicou.data,
                              outras_indicacoes=formlogin.outras_indicacoes.data)
            database.session.add(usuarioo)
            database.session.commit()
            return redirect(url_for('info2'))  # Redireciona para a próxima página após o envio
    return render_template("homepage.html", form=formlogin)

@app.route("/info2", methods=["GET", "POST"])
def info2():
    form2 = FormPagina2()
    if form2.validate_on_submit():
        info = Info(objetivoimediato=form2.objetivo_imediato.data,
                    objetivo_imediato_outras=form2.objetivo_imediato_outras.data,
                    objetivo3a5anos=form2.objetivo_3a5_anos.data,
                    objetivo_3a5_anos_outras=form2.objetivo_3a5_anos_outras.data,
                    objetivo5a10anos=form2.objetivo_5a10_anos.data,
                    objetivo_5a10_anos_outras=form2.objetivo_5a10_anos_outras.data,
                    usuario_id=1)  # Insira o ID do usuário adequado aqui
        database.session.add(info)
        database.session.commit()
        return redirect(url_for('info3'))  # Redireciona para a próxima página após o envio
    return render_template("info2.html", form=form2)


@app.route("/info3", methods=["GET", "POST"])
def info3():
    form3 = FormPagina3()
    if form3.validate_on_submit():
        # Salva os dados do formulário no banco de dados
        info3 = OutraInfo(idadehoje=form3.idade_hoje.data,
                          valorinvestido=form3.valor_investido.data,
                          pouparmes=form3.poupar_mes.data,
                          idadeaposentar=form3.idade_aposentar.data,
                          rendaaposentar=form3.renda_aposentar.data,
                          risco=form3.tolerancia_risco.data,
                          usuario_id=1)  # Insira o ID do usuário adequado aqui
        database.session.add(info3)
        database.session.commit()
        # Redireciona para a página de resultados após o envio
        return redirect(
            url_for('resultados'))

    return render_template("info3.html", form=form3)


@app.route("/resultados", methods=["GET", "POST"])
def resultados():
    mensagem_de_resultado = "Seus resultados estão aqui!"
    return render_template("resultados.html", resultado=mensagem_de_resultado)
