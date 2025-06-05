from models.despesa import Despesa

class DespesaController:
    @staticmethod
    def cadastrar(idplaca, descricao, valor, idprestador, data_servico):
        Despesa.cadastrar(idplaca, descricao, valor, idprestador, data_servico)
    
    @staticmethod
    def listar():
        return Despesa.listar()
    
    @staticmethod
    def alterar(iddespesa, idplaca, descricao, valor, idprestador, data_servico):
        Despesa.alterar(iddespesa, idplaca, descricao, valor, idprestador, data_servico)