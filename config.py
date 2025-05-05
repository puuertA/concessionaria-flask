import pymysql

MYSQL_HOST = '177.190.74.69'
MYSQL_PORT = 65004
MYSQL_USER = 'trabtpc'
MYSQL_PASSWORD = 'trabtpc'
MYSQL_DB = 'tpc15'

def conectar():
    conexao = pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,  # Incluindo a porta
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )

    with conexao.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DB}")
        cursor.execute(f"USE {MYSQL_DB}")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                codcliente INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                endereco VARCHAR(200)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produto (
                codproduto INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                preco DECIMAL(10,2)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS venda (
                codvenda INT AUTO_INCREMENT PRIMARY KEY,
                data DATE,
                valor_total DECIMAL(10,2),
                codcliente INT,
                FOREIGN KEY (codcliente) REFERENCES cliente(codcliente)
                    ON DELETE CASCADE ON UPDATE CASCADE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS itemvenda (
                codvenda INT,
                codproduto INT,
                qtde INT,
                valor DECIMAL(10,2),
                FOREIGN KEY (codvenda) REFERENCES venda(codvenda)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (codproduto) REFERENCES produto(codproduto)
                    ON DELETE CASCADE ON UPDATE CASCADE
            )
        """)

    return pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,  # Incluindo a porta
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB,
        cursorclass=pymysql.cursors.DictCursor
    )
