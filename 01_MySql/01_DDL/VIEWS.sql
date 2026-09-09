-- MySQL view example code
CREATE OR REPLACE VIEW customer_order_summary AS
SELECT c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    COUNT(o.order_id) AS total_orders,
    COALESCE(SUM(o.total_amount), 0) AS total_spend
FROM customers c
    LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id,
    c.first_name,
    c.last_name;
-- Example usage:
SELECT *
FROM customer_order_summary;