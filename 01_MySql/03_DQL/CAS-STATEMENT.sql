-- ====================================================================
-- CASE EXPRESSIONS, COALESCE, AND NULLIF
-- ====================================================================

-- 1. SIMPLE CASE EXPRESSION
-- Compares product_name with fixed values and converts product names into readable types.
SELECT product_name,
       CASE product_name
           WHEN 'SQL Book' THEN 'Book'
           WHEN 'Laptop' THEN 'Electronics'
           WHEN 'T-Shirt' THEN 'Clothing'
           ELSE 'Other'
       END AS product_type
FROM products;


-- 2. SEARCHED CASE EXPRESSION
-- Evaluates conditions in order to classify orders into tiers based on their total amount.
SELECT order_id,
       total_amount,
       CASE
           WHEN total_amount >= 1000 THEN 'Premium'
           WHEN total_amount >= 500 THEN 'Standard'
           WHEN total_amount > 0 THEN 'Basic'
           ELSE 'Invalid'
       END AS order_tier
FROM orders;


-- 3. COALESCE FUNCTION
-- Returns the first non-NULL value. Replaces a missing category_id with 0.
SELECT product_name,
       COALESCE(category_id, 0) AS category_id
FROM products;


-- 4. NULLIF FUNCTION
-- Returns NULL when both expressions are equal. Prevents a zero total_amount from being treated as valid.
SELECT order_id,
       NULLIF(total_amount, 0) AS non_zero_total_amount
FROM orders;


-- 5. CASE IN AN AGGREGATE QUERY
-- Counts total orders and conditionally counts completed and cancelled orders using SUM with CASE.
SELECT COUNT(*) AS total_orders,
       SUM(
           CASE
               WHEN status = 'Completed' THEN 1
               ELSE 0
           END
       ) AS completed_orders,
       SUM(
           CASE
               WHEN status = 'Cancelled' THEN 1
               ELSE 0
           END
       ) AS cancelled_orders
FROM orders;