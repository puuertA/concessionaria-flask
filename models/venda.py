from config import conectar

class Venda:
    @staticmethod
    def cadastrar(data, valor_total, codcliente):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute(
                "INSERT INTO venda (data, valor_total, codcliente) VALUES (%s, %s, %s)",
                (data, valor_total, codcliente)
            )
            codvenda = cursor.lastrowid
        conexao.commit()
        conexao.close()
        return codvenda

    @staticmethod
    def listar():
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT v.codvenda, v.data, v.valor_total, c.nome AS cliente
                FROM venda v
                JOIN cliente c ON v.codcliente = c.codcliente
            """)
            vendas = cursor.fetchall()
        conexao.close()
        return vendas
