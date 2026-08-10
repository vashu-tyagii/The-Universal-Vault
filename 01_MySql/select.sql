-- ====================================================================
-- SELECT STATEMENT & MODIFIERS (Distinct, Alias, Limit, Offset)
-- ====================================================================

-- 1. BASIC SELECT STATEMENT
-- Retrieves all columns and rows from the specified table.
SELECT * 
FROM employees;


-- 2. SELECT WITH DISTINCT
-- Removes duplicate rows from the result set, returning only unique values.
SELECT DISTINCT department_name 
FROM employees;


-- 3. SELECT WITH COLUMN ALIAS (AS)
-- Renames a column temporarily in the output for better readability.
SELECT first_name AS employee_first_name, 
       salary * 12 AS annual_salary 
FROM employees;


-- 4. SELECT WITH TABLE ALIAS
-- Assigns a temporary short name to a table, very useful in JOIN operations.
SELECT e.first_name, e.salary 
FROM employees AS e;


-- 5. SELECT WITH LIMIT
-- Restricts the number of rows returned by the query.
SELECT * 
FROM employees 
LIMIT 5; 
-- Retrieves only the first 5 rows from the table.


-- 6. SELECT WITH LIMIT AND OFFSET
-- Used for pagination. OFFSET skips a specified number of rows before starting to return rows.
SELECT * 
FROM employees 
LIMIT 5 OFFSET 10; 
-- Skips the first 10 rows and then retrieves the next 5 rows (rows 11 through 15).