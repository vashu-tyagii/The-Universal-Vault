-- ====================================================================
-- ORDER BY CLAUSE & SORTING DATA
-- ====================================================================

-- 1. ASCENDING ORDER (DEFAULT)
-- Sorts the result set in ascending order (lowest to highest). ASC is optional.
SELECT *
FROM employees
ORDER BY salary ASC;


-- 2. DESCENDING ORDER
-- Sorts the result set in descending order (highest to lowest).
SELECT *
FROM employees
ORDER BY salary DESC;


-- 3. SORT BY MULTIPLE COLUMNS
-- Sorts primarily by department ascending, and then by salary descending within each department.
SELECT *
FROM employees
ORDER BY department ASC, salary DESC;


-- 4. SORT BY CALCULATED EXPRESSION / ALIAS
-- Sorts the query results using a custom alias or calculated expression.
SELECT first_name, 
       last_name, 
       salary * 12 AS annual_salary
FROM employees
ORDER BY annual_salary DESC;


-- 5. SORT WITH NULL VALUES LAST
-- Forces rows with NULL values in the salary column to appear at the very end of the result set.
SELECT *
FROM employees
ORDER BY (salary IS NULL), salary ASC;