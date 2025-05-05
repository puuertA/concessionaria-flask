from flask import Flask, render_template, request, redirect, url_for
from models.cliente import Cliente
from models.produto import Produto
from models.venda import Venda
from models.itemvenda import ItemVenda
from controllers.cliente_controller import ClienteController
from controllers.produto_controller import ProdutoController
from controllers.venda_controller import VendaController
from controllers.itemvenda_controller import ItemVendaController
import config

# Configuração do Flask para localizar os templates na estrutura correta
app = Flask(__name__,
            template_folder='templates')

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# ----- CLIENTE -----
@app.route('/clientes')
def listar_clientes():
    clientes = ClienteController.listar()
    return render_template('listar_clientes.html', clientes=clientes)

@app.route('/clientes/cadastrar', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        ClienteController.cadastrar(nome, endereco)
        return redirect(url_for('listar_clientes'))
    return render_template('cliente_form.html')

# ----- PRODUTO -----
@app.route('/produtos')
def listar_produtos():
    produtos = ProdutoController.listar()
    return render_template('listar_produtos.html', produtos=produtos)

@app.route('/produtos/cadastrar', methods=['GET', 'POST'])
def cadastrar_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        ProdutoController.cadastrar(nome, preco)
        return redirect(url_for('listar_produtos'))
    return render_template('produto_form.html')

# ----- VENDA -----
@app.route('/vendas')
def listar_vendas():
    vendas = VendaController.listar()
    return render_template('listar_vendas.html', vendas=vendas)

@app.route('/vendas/cadastrar', methods=['GET', 'POST'])
def cadastrar_venda():
    if request.method == 'POST':
        data = request.form['data']
        codcliente = int(request.form['codcliente'])

        # Receber múltiplos produtos (requer o uso de arrays no form HTML)
        produtos = request.form.getlist('codproduto')
        qtde = request.form.getlist('qtde')
        valor = request.form.getlist('valor')

        itens = []
        for i in range(len(produtos)):
            itens.append({
                'codproduto': int(produtos[i]),
                'qtde': int(qtde[i]),
                'valor': float(valor[i])
            })

        VendaController.cadastrar(data, codcliente, itens)
        return redirect(url_for('listar_vendas'))

    clientes = ClienteController.listar()
    produtos = ProdutoController.listar()
    return render_template('venda_form.html', clientes=clientes, produtos=produtos)

@app.route('/vendas/<int:codvenda>')
def detalhes_venda(codvenda):
    itens = VendaController.listar_itens(codvenda)

    # Calcular o total da venda
    total = sum(item['qtde'] * item['valor'] for item in itens)

    return render_template('detalhes_venda.html', itens=itens, codvenda=codvenda, total=total)

if __name__ == '__main__':
    app.run(debug=True)