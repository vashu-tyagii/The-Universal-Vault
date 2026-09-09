-- MySQL CTE example
-- Common Table Expressions (CTEs) help break complex queries into readable steps.

-- Example tables: customers and orders
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Insert sample data
INSERT INTO customers (customer_id, customer_name, city)
VALUES
    (1, 'Alice', 'New York'),
    (2, 'Bob', 'Chicago'),
    (3, 'Charlie', 'Boston');

INSERT INTO orders (order_id, customer_id, order_date, total_amount)
VALUES
    (101, 1, '2024-01-10', 250.00),
    (102, 1, '2024-02-15', 300.00),
    (103, 2, '2024-02-20', 120.00),
    (104, 3, '2024-03-01', 980.00),
    (105, 2, '2024-03-15', 175.00);

-- CTE: total sales per customer
WITH customer_totals AS (
    SELECT
        c.customer_id,
        c.customer_name,
        SUM(o.total_amount) AS total_spent
    FROM customers c
    LEFT JOIN orders o ON o.customer_id = c.customer_id
    GROUP BY c.customer_id, c.customer_name
),
ranked_customers AS (
    SELECT
        customer_id,
        customer_name,
        total_spent,
        RANK() OVER (ORDER BY total_spent DESC) AS rank_position
    FROM customer_totals
)
SELECT
    customer_id,
    customer_name,
    total_spent,
    rank_position
FROM ranked_customers
WHERE rank_position <= 3;

-- Recursive CTE example: generate numbers from 1 to 10
WITH RECURSIVE numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1
    FROM numbers
    WHERE n < 10
)
SELECT n
FROM numbers;
