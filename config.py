import pymysql

MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'ifsp'
MYSQL_DB = 'dbconcessionaria'

def conectar():
    conexao = pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )

    with conexao.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DB}")
        cursor.execute(f"USE {MYSQL_DB}")

        # Remover todas as tabelas antigas primeiro (na ordem correta devido às foreign keys)
        cursor.execute("DROP TABLE IF EXISTS despesa")
        cursor.execute("DROP TABLE IF EXISTS compra")
        cursor.execute("DROP TABLE IF EXISTS venda")
        cursor.execute("DROP TABLE IF EXISTS itemvenda")
        cursor.execute("DROP TABLE IF EXISTS prestador")
        cursor.execute("DROP TABLE IF EXISTS veiculo")
        cursor.execute("DROP TABLE IF EXISTS produto")
        cursor.execute("DROP TABLE IF EXISTS cliente")

        # Criar tabelas na ordem correta (tabelas sem foreign keys primeiro)
        
        # Tabela cliente
        cursor.execute("""
            CREATE TABLE cliente (
                idcliente INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(60),
                endereco VARCHAR(100),
                cidade VARCHAR(80),
                uf VARCHAR(2),
                cep VARCHAR(9)
            )
        """)

        # Tabela veiculo
        cursor.execute("""
            CREATE TABLE veiculo (
                idplaca VARCHAR(9) PRIMARY KEY,
                ano INT,
                modelo INT,
                preco_fipe DECIMAL(10,2),
                fabricante VARCHAR(50),
                modelo_veiculo VARCHAR(60),
                cor VARCHAR(20),
                preco_venda DECIMAL(10,2),
                total_despesa DECIMAL(10,2)
            )
        """)

        # Tabela prestador
        cursor.execute("""
            CREATE TABLE prestador (
                idprestador INT AUTO_INCREMENT PRIMARY KEY,
                nome_empresa VARCHAR(60),
                cidade VARCHAR(80),
                uf VARCHAR(2),
                cep VARCHAR(9)
            )
        """)

        # Tabela venda (com foreign keys)
        cursor.execute("""
            CREATE TABLE venda (
                idvenda INT AUTO_INCREMENT PRIMARY KEY,
                data DATE,
                valor_vendido DECIMAL(10,2),
                idcliente INT,
                idplaca VARCHAR(9),
                forma_pagamento VARCHAR(40),
                FOREIGN KEY (idcliente) REFERENCES cliente(idcliente)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (idplaca) REFERENCES veiculo(idplaca)
                    ON DELETE CASCADE ON UPDATE CASCADE
            )
        """)

        # Tabela compra (com foreign keys)
        cursor.execute("""
            CREATE TABLE compra (
                idcompra INT AUTO_INCREMENT PRIMARY KEY,
                idplaca VARCHAR(9),
                idcliente INT,
                data DATE,
                valor_pago DECIMAL(10,2),
                forma_pagamento VARCHAR(40),
                FOREIGN KEY (idplaca) REFERENCES veiculo(idplaca)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (idcliente) REFERENCES cliente(idcliente)
                    ON DELETE CASCADE ON UPDATE CASCADE
            )
        """)

        # Tabela despesa (com foreign keys)
        cursor.execute("""
            CREATE TABLE despesa (
                iddespesa INT AUTO_INCREMENT PRIMARY KEY,
                idplaca VARCHAR(9),
                descricao VARCHAR(80),
                valor DECIMAL(10,2),
                idprestador INT,
                data_servico DATE,
                FOREIGN KEY (idplaca) REFERENCES veiculo(idplaca)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (idprestador) REFERENCES prestador(idprestador)
                    ON DELETE CASCADE ON UPDATE CASCADE
            )
        """)

    return pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB,
        cursorclass=pymysql.cursors.DictCursor
    )