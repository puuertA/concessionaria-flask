from models.venda import Venda
from models.itemvenda import ItemVenda

class VendaController:
    @staticmethod
    def cadastrar(data, codcliente, itens):
        # itens: lista de dicionários com 'codproduto', 'qtde', 'valor'
        valor_total = sum(item['qtde'] * item['valor'] for item in itens)
        codvenda = Venda.cadastrar(data, valor_total, codcliente)

        for item in itens:
            ItemVenda.cadastrar(
                codvenda=codvenda,
                codproduto=item['codproduto'],
                qtde=item['qtde'],
                valor=item['valor']
            )

        return codvenda

    @staticmethod
    def listar():
        return Venda.listar()

    @staticmethod
    def listar_itens(codvenda):
        return ItemVenda.listar_por_venda(codvenda)
