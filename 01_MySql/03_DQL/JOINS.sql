-- ====================================================================
-- SQL JOINS CHEAT SHEET (INNER, LEFT, RIGHT, FULL, CROSS, SELF)
-- ====================================================================


-- ====================================================================
-- 1. INNER JOIN
-- ====================================================================
-- Definition: Returns only the records that have matching values in both tables.
-- Any rows with no match in the related table are excluded.

SELECT c.customer_id,
       o.order_id
FROM customers AS c
    INNER JOIN orders AS o ON c.customer_id = o.customer_id;


-- ====================================================================
-- 2. LEFT JOIN (LEFT OUTER JOIN)
-- ====================================================================
-- Definition: Returns all records from the left table, and the matched records 
-- from the right table. If there is no match, the result is NULL on the right side.

SELECT c.customer_id,
       o.order_id
FROM customers AS c
    LEFT JOIN orders AS o ON c.customer_id = o.customer_id;


-- ====================================================================
-- 3. RIGHT JOIN (RIGHT OUTER JOIN)
-- ====================================================================
-- Definition: Returns all records from the right table, and the matched records 
-- from the left table. If there is no match, the result is NULL on the left side.

SELECT c.customer_id,
       o.order_id
FROM customers AS c
    RIGHT JOIN orders AS o ON c.customer_id = o.customer_id;


-- ====================================================================
-- 4. FULL OUTER JOIN
-- ====================================================================
-- Definition: Returns all records when there is a match in either left or right 
-- table records. (Note: MySQL does not support FULL OUTER JOIN directly, 
-- so we simulate it using UNION of LEFT JOIN and RIGHT JOIN).

SELECT c.customer_id,
       o.order_id
FROM customers AS c
    LEFT JOIN orders AS o ON c.customer_id = o.customer_id
UNION
SELECT c.customer_id,
       o.order_id
FROM customers AS c
    RIGHT JOIN orders AS o ON c.customer_id = o.customer_id;


-- ====================================================================
-- 5. CROSS JOIN
-- ====================================================================
-- Definition: Returns the Cartesian product of the two tables—meaning every row 
-- from the first table is combined with every row from the second table.

SELECT c.customer_id,
       o.order_id
FROM customers AS c
    CROSS JOIN orders AS o;


-- ====================================================================
-- 6. SELF JOIN
-- ====================================================================
-- Definition: A regular join, but the table is joined with itself. 
-- Useful for hierarchical data, such as finding an employee's manager in the same table.

SELECT e.employee_id,
       e.name,
       m.name AS manager_name
FROM employees AS e
    LEFT JOIN employees AS m ON e.manager_id = m.employee_id;