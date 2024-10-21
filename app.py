from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('fechamento_caixa_simples.html')

app.run()