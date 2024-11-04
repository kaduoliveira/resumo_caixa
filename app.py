from flask import Flask, render_template, url_for, redirect, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

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

    caixa1 = request.form['caixa1']
    caixa2 = request.form['caixa2']
    caixa3 = request.form['caixa3']
    caixa4 = request.form['caixa4']

    dinheiro1 = request.form['dinheiro1']
    dinheiro2 = request.form['dinheiro2']
    dinheiro3 = request.form['dinheiro3']
    dinheiro4 = request.form['dinheiro4']
    dinheiro_total = request.form['dinheiro_total']

    cartao_cred1 = request.form['cartao_cred1']
    cartao_cred2 = request.form['cartao_cred2']
    cartao_cred3 = request.form['cartao_cred3']
    cartao_cred4 = request.form['cartao_cred4']
    cartao_cred_total = request.form['cartao_cred_total']

    cartao_deb1 = request.form['cartao_deb1']
    cartao_deb2 = request.form['cartao_deb2']
    cartao_deb3 = request.form['cartao_deb3']
    cartao_deb4 = request.form['cartao_deb4']
    cartao_deb_total = request.form['cartao_deb_total']

    pix1 = request.form['pix1']
    pix2 = request.form['pix2']
    pix3 = request.form['pix3']
    pix4 = request.form['pix4']
    pix_total = request.form['pix_total']

    cheque1 = request.form['cheque1']
    cheque2 = request.form['cheque2']
    cheque3 = request.form['cheque3']
    cheque4 = request.form['cheque4']
    cheque_total = request.form['cheque_total']

    total1 = request.form['total1']
    total2 = request.form['total2']
    total3 = request.form['total3']
    total4 = request.form['total4']
    total_total = request.form['total_total']
    
    malote1 = request.form['malote1']
    malote2 = request.form['malote2']
    malote3 = request.form['malote3']
    malote4 = request.form['malote4']
    malote_total = request.form['malote_total']

    sangria1 = request.form['sangria1']
    sangria2 = request.form['sangria2']
    sangria3 = request.form['sangria3']
    sangria4 = request.form['sangria4']
    sangria_total = request.form['sangria_total']

    resultado1 = request.form['resultado1']
    resultado2 = request.form['resultado2']
    resultado3 = request.form['resultado3']
    resultado4 = request.form['resultado4']
    resultado_total = request.form['resultado_total']

    qtd_vendas = request.form['qtd_vendas']

    tkt_medio = request.form['tkt_medio']

    servicos1 = request.form['servicos1']
    servicos2 = request.form['servicos2']
    servicos3 = request.form['servicos3']
    servicos4 = request.form['servicos4']
    servicos_total = request.form['servicos_total']

    print(data)
    data_comparada = Caixas.query.filter_by(data=data).first()
    print(data_comparada.data)
    data_comparada = data_comparada.data
    print(data_comparada)
    if data_comparada.data == data:
        flash('Já existe um caixa salvo para essa data.')
        return redirect(url_for(index))
    
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
    return redirect(url_for('index'))

# Rota para a página de login
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
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
        flash('Olá, {usuario}. Seja bem vindo!'.format(usuario=usuario))
        print('Usuario logado: {usuario}'.format(usuario=usuario))
        if proxima_pagina == 'None':
            proxima_pagina = '/'
        return redirect(proxima_pagina)
    # Caso as senhas sejam diferentes, o usuario é redirecionado para a página de login com uma mensagem de erro
    else:
        flash('Não foi possível fazer o login. Tente novamente')
        return redirect(url_for('login'))

# Rota para logout    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
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

if __name__ == '__main__':
    app.run(debug=True)
