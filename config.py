# Definindo a chave secreta do app, substituiu o app.secret_key = 'segredo_do_app' do app.py
SECRET_KEY = 'segredo_do_app'

# Definindo a URI do banco de dados
SQLALCHEMY_DATABASE_URI = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = 'sumimasen',
    servidor = 'localhost',
    database = 'caixa'
)