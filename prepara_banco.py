import mysql.connector
from mysql.connector import errorcode


print("Conectando...")

# Criando uma conexão com o banco de dados
try:
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'sumimasen'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Existe algo errado no nome de usuário ou senha")
    else:
        print(err)

# Criando um cursor e executando uma query
cursor = conn.cursor()

# Executando uma query, criando um banco de dados
cursor.execute("DROP DATABASE IF EXISTS `caixa`")
cursor.execute("CREATE DATABASE `caixa`")
cursor.execute("USE `caixa`")

# Executando uma query, criando uma tabela
cursor.execute("DROP TABLE IF EXISTS caixas")
cursor.execute('''
            CREATE table caixas (
               id int(11) NOT NULL AUTO_INCREMENT,
               data date NOT NULL,
               caixa1 int(11) NOT NULL,
               caixa2 int(11),
               caixa3 int(11),
               caixa4 int(11),
               dinheiro1 DECIMAL(10, 2),
               dinheiro2 DECIMAL(10, 2),
               dinheiro3 DECIMAL(10, 2),
               dinheiro4 DECIMAL(10, 2),
               dinheiro_total DECIMAL(10, 2),
               cartao_cred1 DECIMAL(10, 2),
               cartao_cred2 DECIMAL(10, 2),
               cartao_cred3 DECIMAL(10, 2),
               cartao_cred4 DECIMAL(10, 2),
               cartao_cred_total DECIMAL(10, 2),
               cartao_deb1 DECIMAL(10, 2),
               cartao_deb2 DECIMAL(10, 2),
               cartao_deb3 DECIMAL(10, 2),
               cartao_deb4 DECIMAL(10, 2),
               cartao_deb_total DECIMAL(10, 2),
               pix1 DECIMAL(10, 2),
               pix2 DECIMAL(10, 2),
               pix3 DECIMAL(10, 2),
               pix4 DECIMAL(10, 2),
               pix_total DECIMAL(10, 2),
               cheque1 DECIMAL(10, 2),
               cheque2 DECIMAL(10, 2),
               cheque3 DECIMAL(10, 2),
               cheque4 DECIMAL(10, 2),
               cheque_total DECIMAL(10, 2),
               total1 DECIMAL(10, 2),
               total2 DECIMAL(10, 2),
               total3 DECIMAL(10, 2),
               total4 DECIMAL(10, 2),
               total_total DECIMAL(10, 2),
               malote1 DECIMAL(10, 2),
               malote2 DECIMAL(10, 2),
               malote3 DECIMAL(10, 2),
               malote4 DECIMAL(10, 2),
               malote_total DECIMAL(10, 2),
               sangria1 DECIMAL(10, 2),
               sangria2 DECIMAL(10, 2),
               sangria3 DECIMAL(10, 2),
               sangria4 DECIMAL(10, 2),
               sangria_total DECIMAL(10, 2),
               resultado1 DECIMAL(10, 2),
               resultado2 DECIMAL(10, 2),
               resultado3 DECIMAL(10, 2),
               resultado4 DECIMAL(10, 2),
               resultado_total DECIMAL(10, 2),
               qtd_vendas int(11),
               tkt_medio DECIMAL(10, 2),
               servicos1 DECIMAL(10, 2),
               servicos2 DECIMAL(10, 2),
               servicos3 DECIMAL(10, 2),
               servicos4 DECIMAL(10, 2),
               servicos_total DECIMAL(10, 2),
               PRIMARY KEY (id)
               ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

cursor.execute("DROP TABLE IF EXISTS usuarios")
cursor.execute('''
               CREATE table usuarios (
               id int(11) NOT NULL AUTO_INCREMENT,
               usuario varchar(40) NOT NULL,
               senha varchar(100) NOT NULL,
               PRIMARY KEY (id)
               ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

# Inserindo dados na tabela
usuarios_sql ='INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)'
usuarios_valores = [
    ("kadu", 123),
    ("caixa", 123)
]

caixas_sql = 'INSERT INTO caixas (data, caixa1, total_total, qtd_vendas, tkt_medio, servicos_total) VALUES (%s, %s, %s, %s, %s, %s)'
caixas_valores = [
    ("2023-01-01", 1, 100, 10, 10, 10),
    ("2023-01-02", 2, 200, 20, 20, 20),
    ("2023-01-03", 3, 300, 30, 30, 30)
]

cursor.executemany(caixas_sql, caixas_valores)
cursor.executemany(usuarios_sql, usuarios_valores)

# Mostrando os dados da tabela caixas
cursor.execute("SELECT data, caixa1, total_total, qtd_vendas, tkt_medio, servicos_total FROM caixas")
print('------------------caixas------------------')
for caixa in cursor.fetchall():
    print(caixa)


# Mostrando os dados da tabela usuarios
cursor.execute("SELECT * FROM usuarios")
print('------------------usuarios------------------')
for usuario in cursor.fetchall():
    print(usuario)

conn.commit()

cursor.close()
conn.close()