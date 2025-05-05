from config import conectar

class Produto:
    @staticmethod
    def cadastrar(nome, preco):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO produto (nome, preco) VALUES (%s, %s)", (nome, preco))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM produto")
            produtos = cursor.fetchall()
        conexao.close()
        return produtos
