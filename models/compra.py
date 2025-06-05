from config import conectar

class Compra:
    @staticmethod
    def cadastrar(idplaca, idcliente, data, valor_pago, forma_pagamento):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO compra (idplaca, idcliente, data, valor_pago, forma_pagamento) VALUES (%s, %s, %s, %s, %s)", 
                         (idplaca, idcliente, data, valor_pago, forma_pagamento))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM compra")
            compras = cursor.fetchall()
        conexao.close()
        return compras
    
    @staticmethod
    def alterar(idcompra, idplaca, idcliente, data, valor_pago, forma_pagamento):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("UPDATE compra SET idplaca=%s, idcliente=%s, data=%s, valor_pago=%s, forma_pagamento=%s WHERE idcompra=%s", 
                         (idplaca, idcliente, data, valor_pago, forma_pagamento, idcompra))
        conexao.commit()
        conexao.close()