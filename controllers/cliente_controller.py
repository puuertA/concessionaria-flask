from models.cliente import Cliente

class ClienteController:
    @staticmethod
    def cadastrar(nome, endereco):
        Cliente.cadastrar(nome, endereco)

    @staticmethod
    def listar():
        return Cliente.listar()
