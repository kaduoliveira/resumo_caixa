from flask import Flask, render_template, url_for, redirect, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false
from datetime import datetime

# Instanciando o app
app = Flask(__name__)

# Carregando as configurações do arquivo config.py
app.config.from_pyfile('config.py')

# Definindo o banco de dados
db = SQLAlchemy(app)

# Define a classe Caixa database
class Caixas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.Date, nullable=False)
    caixa1 = db.Column(db.Integer, nullable=False)
    caixa2 = db.Column(db.Integer, nullable=True)
    caixa3 = db.Column(db.Integer, nullable=True)
    caixa4 = db.Column(db.Integer, nullable=True)
    dinheiro1 = db.Column(db.Float, nullable=True)
    dinheiro2 = db.Column(db.Float, nullable=True)
    dinheiro3 = db.Column(db.Float, nullable=True)
    dinheiro4 = db.Column(db.Float, nullable=True)
    dinheiro_total = db.Column(db.Float, nullable=True)
    cartao_cred1 = db.Column(db.Float, nullable=True)
    cartao_cred2 = db.Column(db.Float, nullable=True)
    cartao_cred3 = db.Column(db.Float, nullable=True)
    cartao_cred4 = db.Column(db.Float, nullable=True)
    cartao_cred_total = db.Column(db.Float, nullable=True)
    cartao_deb1 = db.Column(db.Float, nullable=True)
    cartao_deb2 = db.Column(db.Float, nullable=True)
    cartao_deb3 = db.Column(db.Float, nullable=True)
    cartao_deb4 = db.Column(db.Float, nullable=True)
    cartao_deb_total = db.Column(db.Float, nullable=True)
    pix1 = db.Column(db.Float, nullable=True)
    pix2 = db.Column(db.Float, nullable=True)
    pix3 = db.Column(db.Float, nullable=True)
    pix4 = db.Column(db.Float, nullable=True)
    pix_total = db.Column(db.Float, nullable=True)
    cheque1 = db.Column(db.Float, nullable=True)
    cheque2 = db.Column(db.Float, nullable=True)
    cheque3 = db.Column(db.Float, nullable=True)
    cheque4 = db.Column(db.Float, nullable=True)
    cheque_total = db.Column(db.Float, nullable=True)
    total1 = db.Column(db.Float, nullable=True)
    total2 = db.Column(db.Float, nullable=True)
    total3 = db.Column(db.Float, nullable=True)
    total4 = db.Column(db.Float, nullable=True)
    total_total = db.Column(db.Float, nullable=True)
    malote1 = db.Column(db.Float, nullable=True)
    malote2 = db.Column(db.Float, nullable=True)
    malote3 = db.Column(db.Float, nullable=True)
    malote4 = db.Column(db.Float, nullable=True)
    malote_total = db.Column(db.Float, nullable=True)
    sangria1 = db.Column(db.Float, nullable=True)
    sangria2 = db.Column(db.Float, nullable=True)
    sangria3 = db.Column(db.Float, nullable=True)
    sangria4 = db.Column(db.Float, nullable=True)
    sangria_total = db.Column(db.Float, nullable=True)
    resultado1 = db.Column(db.Float, nullable=True)
    resultado2 = db.Column(db.Float, nullable=True)
    resultado3 = db.Column(db.Float, nullable=True)
    resultado4 = db.Column(db.Float, nullable=True)
    resultado_total = db.Column(db.Float, nullable=True)
    qtd_vendas = db.Column(db.Integer, nullable=True)
    tkt_medio = db.Column(db.Float, nullable=True)
    servicos1 = db.Column(db.Float, nullable=True)
    servicos2 = db.Column(db.Float, nullable=True)
    servicos3 = db.Column(db.Float, nullable=True)
    servicos4 = db.Column(db.Float, nullable=True)
    servicos_total = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'id: {self.id} - Caixa nº.: {self.caixa1} - Data: {self.data} - Total Vendas: {self.total_total} - Serviços: {self.servicos_total}'
    
class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(40), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'id: {self.id} - Usuario: {self.usuario} - Senha: {self.senha}'
    
# Rota principal
@app.route('/')
def index():
    # Efetuando uma query direto no banco que vai recber uma lista ordenada pelo id
    lista = Caixas.query.order_by(Caixas.id)
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

# Rota para a página de login
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if session['usuario_logado'] is not None:
        flash('Usuario -- {usuario_logado} -- já está logado'.format(usuario_logado=session['usuario_logado']))
        return redirect(url_for('index'))
    return render_template('login.html', proxima=proxima)

# Rota para autenticar o login
@app.route('/autenticar', methods=['POST', ])
def autenticar():
    # Comparando o valor presente no banco de dados com o obtido no formulario, essa query retorna um True/False
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

@app.route('/editar/<int:id>')
def editar(id):
    pass
    '''# Verificando se o usuario está logando antes de continuar
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print('Redirecionado pro login.')
        return redirect(url_for('login', proxima=url_for('editar')))
    caixa = Caixa.query.filter_by(id=id).first()
    return render_template('editar.html', caixa=caixa)'''

''' # Esse trecho de código substitui o logo a seguir e possibilita a aplicação a rodar acessando de outras maquinas na rede
if __name__ == '__main__':
    app.run(debug=True, host='192.168.15.110')
'''
if __name__ == '__main__':
    app.run(debug=True)
