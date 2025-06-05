from models.venda import Venda

class VendaController:
    @staticmethod
    def cadastrar(data, valor_vendido, idcliente, idplaca, forma_pagamento):
        Venda.cadastrar(data, valor_vendido, idcliente, idplaca, forma_pagamento)
    
    @staticmethod
    def listar():
        return Venda.listar()
    
    @staticmethod
    def alterar(idvenda, data, valor_vendido, idcliente, idplaca, forma_pagamento):
        Venda.alterar(idvenda, data, valor_vendido, idcliente, idplaca, forma_pagamento)