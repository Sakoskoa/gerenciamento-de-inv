from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def connect_db():
    return sqlite3.connect('inventario.sql')

# Rota para a página principal (Interface)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para adicionar um produto
@app.route('/produtos', methods=['POST'])
def add_produto():
    data = request.get_json()  # Recebe os dados do produto
    nome = data['nome']
    descricao = data['descricao']
    preco = data['preco']
    quantidade = data['quantidade']
    
    # Conecta ao banco de dados
    conn = connect_db()
    cursor = conn.cursor()
    
    # Insere o produto no banco de dados
    cursor.execute('''
        INSERT INTO produtos (nome, descricao, preco, quantidade)
        VALUES (?, ?, ?, ?)
    ''', (nome, descricao, preco, quantidade))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Produto adicionado com sucesso!"}), 201

# Rota para listar todos os produtos
@app.route('/produtos', methods=['GET'])
def get_produtos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    
    # Retorna os produtos no formato JSON
    return jsonify(produtos)

# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
