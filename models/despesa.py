from config import conectar

class Despesa:
    @staticmethod
    def cadastrar(idplaca, descricao, valor, idprestador, data_servico):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO despesa (idplaca, descricao, valor, idprestador, data_servico) VALUES (%s, %s, %s, %s, %s)", 
                         (idplaca, descricao, valor, idprestador, data_servico))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM despesa")
            despesas = cursor.fetchall()
        conexao.close()
        return despesas
    
    @staticmethod
    def alterar(iddespesa, idplaca, descricao, valor, idprestador, data_servico):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("UPDATE despesa SET idplaca=%s, descricao=%s, valor=%s, idprestador=%s, data_servico=%s WHERE iddespesa=%s", 
                         (idplaca, descricao, valor, idprestador, data_servico, iddespesa))
        conexao.commit()
        conexao.close()