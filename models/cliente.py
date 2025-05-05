from config import conectar

class Cliente:
    @staticmethod
    def cadastrar(nome, endereco):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO cliente (nome, endereco) VALUES (%s, %s)", (nome, endereco))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM cliente")
            clientes = cursor.fetchall()
        conexao.close()
        return clientes
