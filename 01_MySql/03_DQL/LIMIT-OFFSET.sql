-- ====================================================================
-- PAGINATION WITH LIMIT AND OFFSET
-- ====================================================================

-- 1. BASIC LIMIT
-- LIMIT restricts the number of rows returned.
SELECT *
FROM employees
LIMIT 10;


-- 2. LIMIT WITH OFFSET
-- OFFSET skips a specified number of rows before returning results.
SELECT *
FROM employees
LIMIT 10 OFFSET 20;


-- 3. ALTERNATE MYSQL PAGINATION SYNTAX
-- MySQL also supports the comma syntax: LIMIT offset, row_count.
SELECT *
FROM employees
LIMIT 20, 10;


-- 4. ORDERED PAGINATION (BEST PRACTICE)
-- Always use ORDER BY with pagination to ensure consistent, predictable results.
SELECT *
FROM employees
ORDER BY employee_id
LIMIT 10 OFFSET 20;