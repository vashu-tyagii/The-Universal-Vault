-- ====================================================================
-- WHERE CLAUSE & FILTERING DATA
-- ====================================================================

-- 1. BASIC WHERE CLAUSE (Numerical Filtering)
-- Filters rows based on a specific numerical condition.
SELECT first_name, salary 
FROM employees 
WHERE salary > 50000;


-- 2. WHERE WITH TEXT / STRING MATCHING
-- Filters rows where a string column matches a specific value.
SELECT first_name, department_name 
FROM employees 
WHERE department_name = 'IT';


-- 3. WHERE WITH COMPARISON OPERATORS
-- Using multiple conditions with AND, OR, and NOT.
SELECT first_name, department_name, salary 
FROM employees 
WHERE department_name = 'HR' AND salary >= 40000;


-- 4. WHERE WITH BETWEEN OPERATOR
-- Filters data within a specific range (inclusive of boundary values).
SELECT first_name, salary 
FROM employees 
WHERE salary BETWEEN 30000 AND 60000;


-- 5. WHERE WITH IN OPERATOR
-- Filters data matching any value inside a specified list.
SELECT first_name, department_name 
FROM employees 
WHERE department_name IN ('IT', 'Finance', 'Marketing');


-- 6. WHERE WITH LIKE OPERATOR (Pattern Matching)
-- Using wildcards: '%' represents zero or more characters, '_' represents a single character.
SELECT first_name 
FROM employees 
WHERE first_name LIKE 'A%'; 
-- Finds all employees whose first name starts with the letter 'A'.


-- 7. WHERE WITH IS NULL / IS NOT NULL
-- Checking for missing or existing values in a column.
SELECT first_name, email 
FROM employees 
WHERE email IS NULL;