from flask import Flask, render_template

app = Flask(__name__)

class Caixa:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.movimentacoes = []


@app.route('/')
def index():

    caixa1 = Caixa(123, '2024-10-20')
    caixa2 = Caixa(456, '2024-10-20')

    lista = [caixa1, caixa2]

    print(caixa1)
    print(caixa2)
    return render_template('lista.html', caixas=lista)



if __name__ == '__main__':
    app.run(debug=True)
