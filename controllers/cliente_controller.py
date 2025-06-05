from models.cliente import Cliente

class ClienteController:
    @staticmethod
    def cadastrar(nome, endereco, cidade, uf, cep):
        Cliente.cadastrar(nome, endereco, cidade, uf, cep)
    
    @staticmethod
    def listar():
        return Cliente.listar()
    
    @staticmethod
    def alterar(idcliente, nome, endereco, cidade, uf, cep):
        Cliente.alterar(idcliente, nome, endereco, cidade, uf, cep)