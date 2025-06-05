from config import conectar

class Cliente:
    @staticmethod
    def cadastrar(nome, endereco, cidade, uf, cep):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO cliente (nome, endereco, cidade, uf, cep) VALUES (%s, %s, %s, %s, %s)", 
                         (nome, endereco, cidade, uf, cep))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM cliente")
            clientes = cursor.fetchall()
        conexao.close()
        return clientes
    
    @staticmethod
    def alterar(idcliente, nome, endereco, cidade, uf, cep):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("UPDATE cliente SET nome=%s, endereco=%s, cidade=%s, uf=%s, cep=%s WHERE idcliente=%s", 
                         (nome, endereco, cidade, uf, cep, idcliente))
        conexao.commit()
        conexao.close()