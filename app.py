from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados

def connect_db():
    return sqlite3.connect('inventario.db')

# Rota para adicionar um novo produto 

@app.route('/produtos', methods=['POST'])
def add_produto():
    data = request.get_json()
    nome = data['nome']
    descricao = data['descricao']
    preco = data ['preco']
    quantidade = data['quantidade']

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO produtos (nome, descricacao, preco, quantidade) VALUES (?, ?, ?, ?)''', (nome,descricao, preco, quantidade))
    conn.commit()
    conn.close()

    return jsonify ({"message": "Produto adicionado com sucesso!"}), 201

# Rota para Listar todos os produtos

@app.route('/produtos', methods=['GET'])
def get_produtos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()

    return jsonify(produtos)

# Iniciar o servidor Flask

if __name__ == '__main__':
    app.run(debug=True)