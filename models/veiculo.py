from config import conectar

class Veiculo:
    @staticmethod
    def cadastrar(idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda=None, total_despesa=None):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO veiculo (idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda, total_despesa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                         (idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda, total_despesa))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM veiculo")
            veiculos = cursor.fetchall()
        conexao.close()
        return veiculos
    
    @staticmethod
    def alterar(idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda=None, total_despesa=None):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("UPDATE veiculo SET ano=%s, modelo=%s, preco_fipe=%s, fabricante=%s, modelo_veiculo=%s, cor=%s, preco_venda=%s, total_despesa=%s WHERE idplaca=%s", 
                         (ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda, total_despesa, idplaca))
        conexao.commit()
        conexao.close()