from flask import Flask, render_template, url_for, request, redirect, flash, session



app = Flask(__name__)

app.config['SECRET_KEY'] = 'segredo_do_app'

class Caixa:
    def __init__(self, id, data, caixa, dinheiro, cartao_cred, cartao_deb, pix, cheque, total, malote, sangria, resultado, qtd_vendas, tkt_medio, servicos):
        self.id = id
        self.data = data
        self.caixa = caixa
        self.dinheiro = dinheiro
        self.cartao_cred = cartao_cred
        self.cartao_deb = cartao_deb
        self.pix = pix
        self.cheque = cheque
        self.total = total
        self.malote = malote
        self.sangria = sangria
        self.resultado = resultado
        self.qtd_vendas = qtd_vendas
        self.tkt_medio = tkt_medio
        self.servicos = servicos
    
    def __str__(self):
        return f'id: {self.id} - Caixa nº.: {self.caixa} - Data: {self.data} - Total Vendas: {self.total} - Serviços: {self.servicos}'

# Criando uma lista de objetos da classe Caixa
lista = []

# Criando objetos da classe Caixa
caixa1 = Caixa(123, '2024-10-20', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
caixa2 = Caixa(456, '2024-10-20', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

lista = [caixa1, caixa2]

@app.route('/')
def index():
    # Imprimindo os objetos da classe Caixa
    for caixa in lista:
        print(caixa)
    return render_template('lista.html', caixas=lista)

@app.route('/novo')
def novo():

    # Verificando se o usuario está logando antes de continuar
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print('Redirecionado pro login.')
        return redirect(url_for('login', proxima=url_for('novo')))

    return render_template('novo.html')

@app.route('/criar', methods=['POST',])
def criar():
   
    # Requisitando os valores do formulário usando o método POST e o método request do Flask 'puro'
    data = request.form['data']
    caixa1 =request.form['caixa1']
    dinheiro1 = request.form['dinheiro1']
    cartao_cred1 = request.form['cartao_cred1']
    cartao_deb1 = request.form['cartao_deb1']
    pix1 = request.form['pix1']
    cheque1 = request.form['cheque1']
    total1 = request.form['total1']
    malote1 = request.form['malote1']
    sangria1 = request.form['sangria1']
    resultado1 = request.form['resultado1']
    qtd_vendas = request.form['qtd_vendas']
    tkt_medio = request.form['tkt_medio']
    servicos1 = request.form['servicos1']

    # Criando um objeto da classe Caixa com os valores do formulário
    caixa = Caixa(id, data, caixa1, dinheiro1, cartao_cred1, cartao_deb1, pix1, cheque1, total1, malote1, sangria1, resultado1, qtd_vendas, tkt_medio, servicos1)

    # Adicionando o objeto da classe Caixa a lista de caixas
    lista.append(caixa)

    # Imprimindo o objeto da classe Caixa
    print(caixa)

    # Retornando a página de lista de caixas
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST', ])
def autenticar():

    # Definindo uma senha padrão
    senha_padrao = '123'

    # Requisitando o valor do campo senha e usuario para comparação
    senha = request.form['senha']
    usuario = request.form['usuario']
    proxima_pagina = request.form['proxima']

    # Comparando senhas e aplicando condicional
    if senha_padrao == senha:

        # requisitando o usuario e mantendo na session para usar no flash
        session['usuario_logado'] = usuario
        flash(f'Olá, {usuario}. Seja bem vindo!')
        return redirect(proxima_pagina)

    else:
        flash('Não foi possível fazer o login. Tente novamente')
        return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)
