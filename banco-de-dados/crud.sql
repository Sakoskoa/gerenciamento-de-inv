INSERT INTO produtos (nome, descricao, preco, quantidade)
VALUES ('Produto A', 'Descrição do Produto A', 100.00, 50);

SELECT * FROM produtos;

UPDATE produtos 
SET preco = 120.00, quantidade = 45 
WHERE id = 1;

DELETE FROM produtos WHERE id = 1;

INSERT INTO vendas (id_produto, quantidade, preco_unitario)
VALUES (1,5,100.00);

UPDATE produtos 
SET quantidade = quantidade - 5
WHERE id = 1;

SELECT p.nome, SUM(v.quantidade) AS total_vendido, SUM(v.quantidade * v.preco_unitario) AS total_vendas 
FROM vendas v
JOIN produtos p ON v.id_produto = p.id
WHERE v.data_venda BETWEEN '2025-01-01' AND '2025-02-01'
GROUP BY p.id;