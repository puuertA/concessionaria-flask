from models.itemvenda import ItemVenda

class ItemVendaController:
    @staticmethod
    def cadastrar(codvenda, codproduto, qtde, valor):
        ItemVenda.cadastrar(codvenda, codproduto, qtde, valor)

    @staticmethod
    def listar_por_venda(codvenda):
        return ItemVenda.listar_por_venda(codvenda)
