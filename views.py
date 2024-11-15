from flask import render_template, url_for, redirect, request, flash, session
from app import app, db
from models import Caixas, Usuarios
from datetime import datetime

# Rota principal
@app.route('/')
def index():
    # Efetuando uma query direto no banco que vai recber uma lista ordenada pelo id
    lista = Caixas.query.order_by(Caixas.data).all()
    print('Listando Caixas presentes no banco de dados') 
    return render_template('lista.html', caixas=lista)

# Rota que leva à página de criação de um novo caixa
@app.route('/novo')
def novo():

    # Verificando se o usuario está logando antes de continuar
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print('Redirecionado pro login.')
        return redirect(url_for('login', proxima=url_for('novo')))

    return render_template('novo.html')

# Rota para criar um novo caixa
@app.route('/criar', methods=['POST',])
def criar():
   
    # Requisitando os valores do formulário usando o método POST e o método request do Flask 'puro'
    
    data = request.form['data']
    print(data)
    print(type(data))
    data_comparada = Caixas.query.filter_by(data=data).first()
    print(data_comparada)
    print(type(data_comparada))

    data_formatada = datetime.strptime(data, '%Y-%m-%d')
    data_comparada = Caixas.query.filter_by(data=data_formatada).first()

    if data_comparada:
        flash('Já existe um caixa salvo para essa data.')
        return redirect(url_for('index'))

    caixa1 = int(request.form['caixa1']) if request.form['caixa1'] != '' else 0
    caixa2 = int(request.form['caixa2']) if request.form['caixa2'] != '' else 0 
    caixa3 = int(request.form['caixa3']) if request.form['caixa3'] != '' else 0
    caixa4 = int(request.form['caixa4']) if request.form['caixa4'] != '' else 0
    print('Caixa  1: {caixa1}, 2: {caixa2}, 3: {caixa3}, 4: {caixa4}'.format(caixa1=caixa1, caixa2=caixa2, caixa3=caixa3, caixa4=caixa4))

    dinheiro1 = float(request.form['dinheiro1']) if request.form['dinheiro1'] != '' else 0
    dinheiro2 = float(request.form['dinheiro2']) if request.form['dinheiro2'] != '' else 0
    dinheiro3 = float(request.form['dinheiro3']) if request.form['dinheiro3'] != '' else 0
    dinheiro4 = float(request.form['dinheiro4']) if request.form['dinheiro4'] != '' else 0
    dinheiro_total = float(request.form['dinheiro_total']) if request.form['dinheiro_total'] != '' else 0
    print('Dinheiro: ', dinheiro1, dinheiro2, dinheiro3, dinheiro4, dinheiro_total)

    cartao_cred1 = float(request.form['cartao_cred1']) if request.form['cartao_cred1'] != '' else 0
    cartao_cred2 = float(request.form['cartao_cred2']) if request.form['cartao_cred2'] != '' else 0
    cartao_cred3 = float(request.form['cartao_cred3']) if request.form['cartao_cred3'] != '' else 0
    cartao_cred4 = float(request.form['cartao_cred4']) if request.form['cartao_cred4'] != '' else 0
    cartao_cred_total = float(request.form['cartao_cred_total']) if request.form['cartao_cred_total'] != '' else 0

    cartao_deb1 = float(request.form['cartao_deb1']) if request.form['cartao_deb1'] != '' else 0
    cartao_deb2 = float(request.form['cartao_deb2']) if request.form['cartao_deb2'] != '' else 0
    cartao_deb3 = float(request.form['cartao_deb3']) if request.form['cartao_deb3'] != '' else 0
    cartao_deb4 = float(request.form['cartao_deb4']) if request.form['cartao_deb4'] != '' else 0
    cartao_deb_total = float(request.form['cartao_deb_total']) if request.form['cartao_deb_total'] != '' else 0

    pix1 = float(request.form['pix1']) if request.form['dinheiro3'] != '' else 0
    pix2 = float(request.form['pix2']) if request.form['dinheiro3'] != '' else 0
    pix3 = float(request.form['pix3']) if request.form['dinheiro3'] != '' else 0
    pix4 = float(request.form['pix4']) if request.form['dinheiro3'] != '' else 0
    pix_total = float(request.form['pix_total']) if request.form['dinheiro3'] != '' else 0

    cheque1 = float(request.form['cheque1']) if request.form['cheque1'] != '' else 0
    cheque2 = float(request.form['cheque2']) if request.form['cheque2'] != '' else 0
    cheque3 = float(request.form['cheque3']) if request.form['cheque3'] != '' else 0
    cheque4 = float(request.form['cheque4']) if request.form['cheque4'] != '' else 0
    cheque_total = float(request.form['cheque_total']) if request.form['cheque_total'] != '' else 0

    total1 = float(request.form['total1']) if request.form['total1'] != '' else 0
    total2 = float(request.form['total2']) if request.form['total2'] != '' else 0
    total3 = float(request.form['total3']) if request.form['total3'] != '' else 0
    total4 = float(request.form['total4']) if request.form['total4'] != '' else 0
    total_total = float(request.form['total_total']) if request.form['total_total'] != '' else 0
    
    malote1 = float(request.form['malote1']) if request.form['malote1'] != '' else 0
    malote2 = float(request.form['malote2']) if request.form['malote2'] != '' else 0
    malote3 = float(request.form['malote3']) if request.form['malote3'] != '' else 0
    malote4 = float(request.form['malote4']) if request.form['malote4'] != '' else 0
    malote_total = float(request.form['malote_total']) if request.form['malote_total'] != '' else 0

    sangria1 = float(request.form['sangria1']) if request.form['sangria1'] != '' else 0
    sangria2 = float(request.form['sangria2']) if request.form['sangria2'] != '' else 0
    sangria3 = float(request.form['sangria3']) if request.form['sangria3'] != '' else 0
    sangria4 = float(request.form['sangria4']) if request.form['sangria4'] != '' else 0
    sangria_total = float(request.form['sangria_total']) if request.form['sangria_total'] != '' else 0

    resultado1 = float(request.form['resultado1']) if request.form['resultado1'] != '' else 0
    resultado2 = float(request.form['resultado2']) if request.form['resultado2'] != '' else 0
    resultado3 = float(request.form['resultado3']) if request.form['resultado3'] != '' else 0
    resultado4 = float(request.form['resultado4']) if request.form['resultado4'] != '' else 0
    resultado_total = float(request.form['resultado_total']) if request.form['resultado_total'] != '' else 0

    qtd_vendas = int(request.form['qtd_vendas']) if request.form['qtd_vendas'] != '' else 0

    tkt_medio = float(request.form['tkt_medio']) if request.form['tkt_medio'] != '' else 0

    servicos1 = request.form['servicos1'] if request.form['servicos1'] != '' else 0
    servicos2 = request.form['servicos2'] if request.form['servicos2'] != '' else 0
    servicos3 = request.form['servicos3'] if request.form['servicos3'] != '' else 0
    servicos4 = request.form['servicos4'] if request.form['servicos4'] != '' else 0
    servicos_total = request.form['servicos_total'] if request.form['servicos_total'] != '' else 0


    # Criando um objeto da classe Caixas com os valores do formulário
    novo_caixa = Caixas(
        data=data,
        caixa1=caixa1, caixa2=caixa2, caixa3=caixa3, caixa4=caixa4,
        dinheiro1=dinheiro1, dinheiro2=dinheiro2, dinheiro3=dinheiro3, dinheiro4=dinheiro4, dinheiro_total=dinheiro_total,
        cartao_cred1=cartao_cred1, cartao_cred2=cartao_cred2, cartao_cred3=cartao_cred3, cartao_cred4=cartao_cred4, cartao_cred_total=cartao_cred_total,
        cartao_deb1=cartao_deb1, cartao_deb2=cartao_deb2, cartao_deb3=cartao_deb3, cartao_deb4=cartao_deb4, cartao_deb_total=cartao_deb_total,
        pix1=pix1, pix2=pix2, pix3=pix3, pix4=pix4, pix_total=pix_total,
        cheque1=cheque1, cheque2=cheque2, cheque3=cheque3, cheque4=cheque4, cheque_total=cheque_total,
        total1=total1, total2=total2, total3=total3, total4=total4, total_total=total_total,
        malote1=malote1, malote2=malote2, malote3=malote3, malote4=malote4, malote_total=malote_total,
        sangria1=sangria1, sangria2=sangria2, sangria3=sangria3, sangria4=sangria4, sangria_total=sangria_total,
        resultado1=resultado1, resultado2=resultado2, resultado3=resultado3, resultado4=resultado4, resultado_total=resultado_total,
        qtd_vendas=qtd_vendas,
        tkt_medio=tkt_medio,
        servicos1=servicos1, servicos2=servicos2, servicos3=servicos3, servicos4=servicos4, servicos_total=servicos_total
    ) 

    # Imprimindo o objeto da classe Caixa
    print(novo_caixa)

    # Adicionando o novo caixa no banco
    db.session.add(novo_caixa)
    db.session.commit()  # Salvando no banco de dados

    # Retornando a página de lista de caixas
    flash('Caixa registrado com sucesso!')
    return redirect(url_for('index'))

# Rota para editar os valores de um caixa já criado
@app.route('/editar/<int:id>')
def editar(id):

    # Verificando se o usuario está logando antes de continuar
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print('Redirecionado pro login.')
        return redirect(url_for('login', proxima=url_for('editar')))
    caixa = Caixas.query.filter_by(id=id).first()
    return render_template('editar.html', caixa=caixa)

# Rota para a página de login
@app.route('/login')
def login():
    proxima = request.args.get('proxima') 
    return render_template('login.html', proxima=proxima)
    '''proxima = request.args.get('proxima')
    if session['usuario_logado'] is not None:
        flash('Usuario -- {usuario_logado} -- já está logado'.format(usuario_logado=session['usuario_logado']))
        return redirect(url_for('index'))
    return render_template('login.html', proxima=proxima)'''

# Rota para autenticar o login
@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = request.form['usuario']
    senha = request.form['senha']
    proxima_pagina = request.form.get('proxima')
    
    usuario_registrado = Usuarios.query.filter_by(usuario=usuario).first()
    
    if usuario_registrado and usuario_registrado.senha == senha:
        session['usuario_logado'] = usuario
        flash(f'Olá, {usuario}. Seja bem-vindo!')
        if not proxima_pagina or proxima_pagina == 'None':
            proxima_pagina = url_for('index')
        return redirect(proxima_pagina)
    else:
        flash('Não foi possível fazer o login. Tente novamente.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

''' # Comparando o valor presente no banco de dados com o obtido no formulario, essa query retorna um True/False
    senha_padrao = Usuarios.query.filter_by(senha=request.form['senha']).first()
    print(senha_padrao)

    # Requisitando o valor do campo senha e usuario para comparação
    senha = request.form['senha']
    usuario = request.form['usuario']
    proxima_pagina = request.form['proxima']

    if senha_padrao:

        # requisitando o usuario e mantendo na session para usar no flash
        session['usuario_logado'] = usuario
        flash('LOGIN completo. Olá, {usuario}. Seja bem vindo!'.format(usuario=usuario))
        print('Usuario logado: {usuario}'.format(usuario=usuario))
        if proxima_pagina == 'None':
            proxima_pagina = '/'
        return redirect(proxima_pagina)
    # Caso as senhas sejam diferentes, o usuario é redirecionado para a página de login com uma mensagem de erro
    else:
        flash('Não foi possível efetuar o login. Tente novamente')
        return redirect(url_for('login'))

# Rota para logout    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('LOGOUT efetuado com sucesso!')
    return redirect(url_for('index'))
    '''

'''@app.route('/editar/<int:id>')
def editar(id):
    pass
    # Verificando se o usuario está logando antes de continuar
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print('Redirecionado pro login.')
        return redirect(url_for('login', proxima=url_for('editar')))
    caixa = Caixa.query.filter_by(id=id).first()
    return render_template('editar.html', caixa=caixa)'''

''' # Esse trecho de código substitui o logo a seguir e possibilita a aplicação a rodar acessando de outras maquinas na rede
if __name__ == '__main__':
    app.run(debug=True, host='192.168.15.110')
'''

@app.route('/atualizar', methods=['POST',])
def atualizar():
    caixa = Caixas.query.filter_by(id=request.form['id']).first()
    
    caixa.caixa1 = request.form['caixa1']
    caixa.caixa2 = request.form['caixa2']
    caixa.caixa3 = request.form['caixa3']
    caixa.caixa4 = request.form['caixa4']

    caixa.dinheiro1 = request.form['dinheiro1']
    caixa.dinheiro2 = request.form['dinheiro2']
    caixa.dinheiro3 = request.form['dinheiro3']
    caixa.dinheiro4 = request.form['dinheiro4']
    caixa.dinheiro_total = request.form['dinheiro_total']

    caixa.cartao_cred1 = request.form['cartao_cred1']
    caixa.cartao_cred2 = request.form['cartao_cred2']
    caixa.cartao_cred3 = request.form['cartao_cred3']
    caixa.cartao_cred4 = request.form['cartao_cred4']
    caixa.cartao_cred_total = request.form['cartao_cred_total']

    caixa.cartao_deb1 = request.form['cartao_deb1']
    caixa.cartao_deb2 = request.form['cartao_deb2']
    caixa.cartao_deb3 = request.form['cartao_deb3']
    caixa.cartao_deb4 = request.form['cartao_deb4']
    caixa.cartao_deb_total = request.form['cartao_deb_total']

    caixa.pix1 = request.form['pix1']
    caixa.pix2 = request.form['pix2']
    caixa.pix3 = request.form['pix3']
    caixa.pix4 = request.form['pix4']
    caixa.pix_total = request.form['pix_total']

    caixa.cheque1 = request.form['cheque1']
    caixa.cheque2 = request.form['cheque2']
    caixa.cheque3 = request.form['cheque3']
    caixa.cheque4 = request.form['cheque4']
    caixa.cheque_total = request.form['cheque_total']

    caixa.total1 = request.form['total1']
    caixa.total2 = request.form['total2']
    caixa.total3 = request.form['total3']
    caixa.total4 = request.form['total4']
    caixa.total_total = request.form['total_total']

    caixa.malote1 = request.form['malote1']
    caixa.malote2 = request.form['malote2']
    caixa.malote3 = request.form['malote3']
    caixa.malote4 = request.form['malote4']
    caixa.malote_total = request.form['malote_total']
    
    caixa.sangria1 = request.form['sangria1']
    caixa.sangria2 = request.form['sangria2']
    caixa.sangria3 = request.form['sangria3']
    caixa.sangria4 = request.form['sangria4']
    caixa.sangria_total = request.form['sangria_total']

    caixa.qtd_vendas = request.form['qtd_vendas']
    caixa.tkt_medio = request.form['tkt_medio']

    caixa.servicos1 = request.form['servicos1']
    caixa.servicos2 = request.form['servicos2']
    caixa.servicos3 = request.form['servicos3']
    caixa.servicos4 = request.form['servicos4']
    caixa.servicos_total = request.form['servicos_total']

    db.session.add(caixa)
    db.session.commit()
    
    flash('Caixa atualizado com sucesso.')
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print('Redirecionando para login antes de acessar o sistema.')
        return redirect(url_for('login'))
    jogo = Caixas.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Caixa deletado com sucesso.')
    return redirect(url_for('index'))