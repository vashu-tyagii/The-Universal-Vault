-- Total salary paid per department.
SELECT department_id,
    SUM(salary) AS dep_Salary
FROM employees
GROUP BY department_id;
-- Average salary per department, rounded to 2 decimal places.
SELECT department_id,
    ROUND(AVG(salary), 2) AS Avg_dep_Salary
FROM employees
GROUP BY department_id;
-- Count of employees per department.
SELECT department_id,
    COUNT(emp_id) AS Total_Emp
FROM employees
GROUP BY department_id;
-- Departments where total salary exceeds 70000 (HAVING).
SELECT department_id,
    SUM(salary) AS dep_Salary
FROM employees
GROUP BY department_id
HAVING SUM(salary) > 70000;
-- Departments with more than 2 employees (HAVING).
SELECT department_id,
    COUNT(emp_id) AS Total_Emp
FROM employees
GROUP BY department_id
HAVING COUNT(emp_id) > 2;
-- Highest-paid employee in each department (hint: think GROUP BY + subquery, or you'll learn a cleaner way with window functions later).
SELECT department_id,
    MAX(salary) AS highest_salary
FROM employees
GROUP BY department_id
ORDER BY highest_salary DESC;
-- Find the department with the lowest average salary.
SELECT department_id,
    MIN(salary) AS lowest_salary
FROM employees
GROUP BY department_id
ORDER BY lowest_salary ASC;
-- Count how many employees earn above 35000, grouped by department.
SELECT COUNT(emp_id),department_id
FROM employees
WHERE salary > 35000
GROUP BY department_id;