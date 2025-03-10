import sqlite3

# Função para conectar ao banco de dados
def connect_db():
    return sqlite3.connect('inventario.sql')

# Função para criar a tabela de produtos
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Criando a tabela 'produtos'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL,
            quantidade INTEGER
        );
    ''')
    conn.commit()
    conn.close()

# Chame a função para criar a tabela
create_table()
print("Banco de dados e tabela criados com sucesso!")
