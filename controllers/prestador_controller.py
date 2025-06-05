from models.prestador import Prestador

class PrestadorController:
    @staticmethod
    def cadastrar(nome_empresa, cidade, uf, cep):
        Prestador.cadastrar(nome_empresa, cidade, uf, cep)
    
    @staticmethod
    def listar():
        return Prestador.listar()
    
    @staticmethod
    def alterar(idprestador, nome_empresa, cidade, uf, cep):
        Prestador.alterar(idprestador, nome_empresa, cidade, uf, cep)