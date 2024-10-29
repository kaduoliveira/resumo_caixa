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
               caixxa2 int(11),
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

cursor.execute("SHOW TABLES")

