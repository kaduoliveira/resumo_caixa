from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false


# Instanciando o app
app = Flask(__name__)

# Carregando as configurações do arquivo config.py
app.config.from_pyfile('config.py')

# Definindo o banco de dados
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True)
