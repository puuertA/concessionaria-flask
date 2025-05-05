from config import conectar

class ItemVenda:
    @staticmethod
    def cadastrar(codvenda, codproduto, qtde, valor):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute(
                "INSERT INTO itemvenda (codvenda, codproduto, qtde, valor) VALUES (%s, %s, %s, %s)",
                (codvenda, codproduto, qtde, valor)
            )
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar_por_venda(codvenda):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT i.codproduto, p.nome, i.qtde, i.valor
                FROM itemvenda i
                JOIN produto p ON i.codproduto = p.codproduto
                WHERE i.codvenda = %s
            """, (codvenda,))
            itens = cursor.fetchall()
        conexao.close()
        return itens
