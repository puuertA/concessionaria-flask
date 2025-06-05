from config import conectar

class Venda:
    @staticmethod
    def cadastrar(data, valor_vendido, idcliente, idplaca, forma_pagamento):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO venda (data, valor_vendido, idcliente, idplaca, forma_pagamento) VALUES (%s, %s, %s, %s, %s)", 
                         (data, valor_vendido, idcliente, idplaca, forma_pagamento))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM venda")
            vendas = cursor.fetchall()
        conexao.close()
        return vendas
    
    @staticmethod
    def alterar(idvenda, data, valor_vendido, idcliente, idplaca, forma_pagamento):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("UPDATE venda SET data=%s, valor_vendido=%s, idcliente=%s, idplaca=%s, forma_pagamento=%s WHERE idvenda=%s", 
                         (data, valor_vendido, idcliente, idplaca, forma_pagamento, idvenda))
        conexao.commit()
        conexao.close()