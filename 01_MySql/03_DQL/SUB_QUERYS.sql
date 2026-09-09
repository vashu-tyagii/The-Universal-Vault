-- ====================================================================
-- 1. SINGLE-ROW SUBQUERY
-- Returns a single value (one row, one column) used with operators like =, >, <
-- Task: Find employees whose salary is greater than the company average.
-- ====================================================================
SELECT emp_id, first_name, job_role, salary 
FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);


-- ====================================================================
-- 2. MULTI-ROW SUBQUERY
-- Returns multiple rows. Used with operators like IN, ANY, ALL.
-- Task: Find employees who work in departments located in 'Bangalore' or 'Hyderabad'.
-- ====================================================================
SELECT emp_id, first_name, department_id, salary 
FROM employees 
WHERE department_id IN (
    SELECT department_id 
    FROM departments 
    WHERE location IN ('Bangalore', 'Hyderabad')
);


-- ====================================================================
-- 3. MULTI-COLUMN SUBQUERY
-- Returns multiple columns to be matched simultaneously.
-- Task: Find employees who have the lowest salary in their respective departments.
-- ====================================================================
SELECT emp_id, first_name, department_id, salary 
FROM employees 
WHERE (department_id, salary) IN (
    SELECT department_id, MIN(salary) 
    FROM employees 
    GROUP BY department_id
);


-- ====================================================================
-- 4. CORRELATED SUBQUERY
-- Depends on the outer query and evaluates row-by-row.
-- Task: Find employees whose salary is higher than their own department's average.
-- ====================================================================
SELECT e1.emp_id, e1.first_name, e1.department_id, e1.salary 
FROM employees e1 
WHERE e1.salary > (
    SELECT AVG(e2.salary) 
    FROM employees e2 
    WHERE e2.department_id = e1.department_id
);


-- ====================================================================
-- 5. NESTED SUBQUERY
-- A subquery inside another subquery.
-- Task: Find employees in Bangalore departments earning more than 90,000.
-- ====================================================================
SELECT first_name, job_role, salary 
FROM employees 
WHERE department_id IN (
    SELECT department_id 
    FROM departments 
    WHERE location = 'Bangalore'
) 
AND salary > 90000;


-- ====================================================================
-- 6. SCALAR SUBQUERY
-- Acts like a single column value expression inside the SELECT clause.
-- Task: Show each employee's details along with the total company staff count.
-- ====================================================================
SELECT first_name, job_role, salary, 
       (SELECT COUNT(*) FROM employees) AS total_company_staff 
FROM employees;


-- ====================================================================
-- 7. INLINE VIEW (DERIVED TABLE)
-- Used inside the FROM clause as a temporary table (must have an alias).
-- Task: Find the average of the maximum salaries per department.
-- ====================================================================
SELECT AVG(max_sal) AS avg_of_max_salaries 
FROM (
    SELECT department_id, MAX(salary) AS max_sal 
    FROM employees 
    GROUP BY department_id
) AS dept_max;