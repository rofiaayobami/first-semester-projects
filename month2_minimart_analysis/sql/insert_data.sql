-- SQL script to insert sample data

INSERT INTO customers (name, email) VALUES ('mubby', 'mubby@yahoo.com'), ('john', 'john@gmail.com'), ('rofiat', 'rofiat@yahoo.com'), ('aishat', 'aishat@gmail.com'), ('rodiat', 'rodiat@gamil.com');

INSERT INTO products (name, price) VALUES ('bodyspray', 12.5), ('Notebook', 5.0), ('nivea', 30.5), ('waterbottle', 15.0), ('chivita', 10.0);

INSERT INTO orders (customer_id, product_id, quantity) VALUES (1, 1, 4), (2, 2, 3),(3, 3, 1), (4, 4, 2), (5, 5, 3) ;

