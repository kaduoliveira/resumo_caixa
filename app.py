from flask import Flask, render_template, url_for, request, redirect, flash, session

# Instanciando o app
app = Flask(__name__)

# Definindo a chave secreta do app, necessária para a sessão(session)
app.config['SECRET_KEY'] = 'segredo_do_app'

# Definindo a classe Caixa
class Caixa:
    def __init__(self, id, data, caixa1, dinheiro1, cartao_cred1, cartao_deb1, pix1, cheque1, total_total, malote1, sangria1, resultado1, qtd_vendas, tkt_medio, servicos1):
        self.id = id
        self.data = data
        self.caixa1 = caixa1
        self.dinheiro1 = dinheiro1
        self.cartao_cred1 = cartao_cred1
        self.cartao_deb1 = cartao_deb1
        self.pix1 = pix1
        self.cheque = cheque1
        self.total_total = total_total
        self.malote1 = malote1
        self.sangria1 = sangria1
        self.resultado1 = resultado1
        self.qtd_vendas = qtd_vendas
        self.tkt_medio = tkt_medio
        self.servicos1 = servicos1

    
    def __str__(self):
        return f'id: {self.id} - Caixa nº.: {self.caixa} - Data: {self.data} - Total Vendas: {self.total} - Serviços: {self.servicos}'

# Criando uma lista de objetos da classe Caixa
lista = []

# Criando objetos da classe Caixa
caixa1 = Caixa(123, '2024-10-20', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
caixa2 = Caixa(456, '2024-10-20', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Adicionando os objetos da classe Caixa na lista
lista = [caixa1, caixa2]

# Rota principal
@app.route('/')
def index():
    # Imprimindo os objetos da classe Caixa
    for caixa in lista:
        print(caixa)
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
    id = request.form['id']
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

    pix1 = request.form['pix1']

    cheque1 = request.form['cheque1']

    total1 = request.form['total1']

    malote1 = request.form['malote1']

    sangria1 = request.form['sangria1']

    resultado1 = request.form['resultado1']

    qtd_vendas = request.form['qtd_vendas']

    tkt_medio = request.form['tkt_medio']

    servicos1 = request.form['servicos1']
    servicos2 = request.form['servicos2']
    servicos3 = request.form['servicos3']
    servicos4 = request.form['servicos4']
    servicos_total = request.form['servicos_total']

    # Criando um objeto da classe Caixa com os valores do formulário
    caixa = Caixa(id, data,
                   caixa1, caixa2, caixa3, caixa4, 
                   dinheiro1, dinheiro2, dinheiro3, dinheiro4, dinheiro_total, 
                   cartao_cred1, 
                   cartao_deb1, 
                   pix1, 
                   cheque1, 
                   total1, 
                   malote1, 
                   sangria1, 
                   resultado1, 
                   qtd_vendas, 
                   tkt_medio, 
                   servicos1, servicos2, servicos3, servicos4, servicos_total)

    # Adicionando o objeto da classe Caixa a lista de caixas
    lista.append(caixa)

    # Imprimindo o objeto da classe Caixa
    print(caixa)

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

    # Definindo uma senha padrão
    senha_padrao = '123'

    # Requisitando o valor do campo senha e usuario para comparação
    senha = request.form['senha']
    usuario = request.form['usuario']
    proxima_pagina = request.form['proxima']

    # Comparando senhas e aplicando condicional
    # Caso as senhas sejam iguais, o usuario é redirecionado para a página de login
    if senha_padrao == senha:

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


if __name__ == '__main__':
    app.run(debug=True)
