-- Select all employees earning more than 35000.
SELECT *
FROM employees
WHERE salary > 35000;
-- Select distinct department_ids from employees.
SELECT DISTINCT *
FROM employees;
-- List employees sorted by salary, highest to lowest.
SELECT *,
    CASE
        WHEN salary > 30000 THEN "Highest"
        ELSE "Lowest"
    END as SalaryRank
FROM employees;
-- Show only the 3 most recently hired employees.
SELECT *
FROM employees
WHERE hire_date > '2026-08-20';
-- Find employees whose email contains "gmail".
SELECT *
FROM employees
WHERE email LIKE '%gmail%';
-- Find employees NOT in department_id 1.
SELECT *
FROM employees
WHERE department_id <> 1;
-- Label each employee "High Salary" (>40000) or "Standard" using CASE.
SELECT *,
    CASE
        WHEN salary > 40000 THEN 'High Salary'
        ELSE 'Standard'
    END AS SalaryRank
FROM employees;
-- Find employees with a NULL value in any column (pick a column to test).
SELECT *
FROM employees
WHERE email IS NULL;