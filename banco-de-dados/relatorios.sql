CREATE TABLE relatorios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(255) NOT NULL,
    data_inicio DATE NOT NULL,
    conteudo TEXT,
    data_geracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);