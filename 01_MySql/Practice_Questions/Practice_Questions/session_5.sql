-- Find the total salary paid per department.
SELECT SUM(salary) AS TotalSalary,
    department_id
FROM employees
GROUP BY department_id
ORDER BY department_id;

-- Find the average salary per department.
SELECT AVG(salary) AS AvgSalary,
    department_id
FROM employees
GROUP BY department_id
ORDER BY department_id;

-- Find the number of employees per department.
SELECT COUNT(emp_id) AS Total_employees,
    department_id
FROM employees
GROUP BY department_id
ORDER BY department_id;

-- Find the highest and lowest salary overall.
SELECT MAX(salary) AS Highest_Salary,
    MIN(salary) AS Lowest_Salary
FROM employees;

-- Find departments where the average salary is above 60000 (use HAVING).
SELECT department_id,
    AVG(salary) AS AvgSalary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 30000;