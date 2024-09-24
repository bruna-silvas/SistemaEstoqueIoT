from flask import Flask, request, jsonify
from repository.produto_repository import ProdutoRepository
from repository.venda_repository import VendaRepository
from model.produto import Produto
from model.venda import Venda

app = Flask(__name__)

produtos = []
vendas = []

@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    data = request.json
    produto = Produto(len(produtos) + 1, data['nome'], data['preco'], data['quantidade'])
    produtos.append(produto)
    return jsonify(produto.__dict__), 201

@app.route('/produtos', methods=['GET'])
def consultar_produtos():
    return jsonify([produto.__dict__ for produto in produtos]), 200

@app.route('/vendas', methods=['POST'])
def registrar_venda():
    data = request.json
    produto_id = data['produto_id']
    quantidade_vendida = data['quantidade']

    produto = next((p for p in produtos if p.id == produto_id), None)
    if produto is None:
        return jsonify({'error': 'Produto não encontrado'}), 404

    if produto.quantidade < quantidade_vendida:
        return jsonify({'error': 'Quantidade insuficiente'}), 400

    venda = Venda(len(vendas) + 1, produto_id, quantidade_vendida, data['data'])
    vendas.append(venda)
    
    produto.quantidade -= quantidade_vendida

    return jsonify(venda.__dict__), 201

@app.route('/vendas', methods=['GET'])
def consultar_vendas():
    return jsonify([venda.__dict__ for venda in vendas]), 200

if __name__ == '__main__':
    app.run(debug=True)
