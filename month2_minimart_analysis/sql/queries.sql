-- SQL queries for retrieving insights
SELECT * 	
From orders as o 
join customers as c on o.customer_id = c.customer_id
join products as p on o.product_id = p.product_id
where c.name = 'rofiat';

SELECT COUNT(*) FROM orders;

SELECT SUM(p.price * o.quantity) AS total_revenue
FROM orders 
JOIN products as p ON o.product_id = p.product_id;

SELECT o.order_id, c.name AS customer, p.name AS product, o.quantity
FROM orders as o 
INNER JOIN customers as c ON o.customer_id = c.customer_id
INNER JOIN products as p ON o.product_id = p.product_id;

SELECT p.name AS product, o.order_id, o.quantity
FROM products as p
LEFT JOIN orders as o ON p.product_id = o.product_id;



