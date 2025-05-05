from models.produto import Produto

class ProdutoController:
    @staticmethod
    def cadastrar(nome, preco):
        Produto.cadastrar(nome, preco)

    @staticmethod
    def listar():
        return Produto.listar()
