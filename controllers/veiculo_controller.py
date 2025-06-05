from models.veiculo import Veiculo

class VeiculoController:
    @staticmethod
    def cadastrar(idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda=None, total_despesa=None):
        Veiculo.cadastrar(idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda, total_despesa)
    
    @staticmethod
    def listar():
        return Veiculo.listar()
    
    @staticmethod
    def alterar(idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda=None, total_despesa=None):
        Veiculo.alterar(idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda, total_despesa)