-- 1. Write a CTE that selects all employees with salary > 35000, then query the CTE to show only their names and salary.
WITH EmpData AS (
    SELECT *
    FROM employees
    WHERE salary > 35000
)
SELECT first_name,
    salary
FROM EmpData;
-- 2. Write a CTE that calculates total salary per department, then use it to find which department has the highest total salary.
WITH SumDepSalary AS (
    SELECT department_id,
        SUM(salary) AS total_salary
    FROM employees
    GROUP BY department_id
)
SELECT department_id,
    total_salary
FROM SumDepSalary
ORDER BY total_salary DESC
LIMIT 1;
-- 3. Write a CTE that calculates average salary per department, then JOIN it back to the employees table to show each employee's
--  salary alongside their department's average.
WITH AvgDepSalary AS (
    SELECT department_id,
        AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT CONCAT(e.first_name, ' ', e.last_name) AS EmpName,
    e.department_id,
    e.salary AS employee_salary,
    ROUND(a.avg_salary, 2) AS dept_average_salary
FROM employees e
    JOIN AvgDepSalary a ON e.department_id = a.department_id;
-- 4. Write two CTEs in a single query — one calculating employee count per department, another calculating total salary per department
--  — then combine both in the final SELECT.
WITH EmpCount AS (
    SELECT department_id,
        COUNT(*) as Emp_Count
    FROM employees
    GROUP BY department_id
),
SumDepSalary AS (
    SELECT department_id,
        SUM(salary) AS total_salary
    FROM employees
    GROUP BY department_id
)
SELECT EC.department_id,
    EC.Emp_Count,
    DC.total_salary
FROM EmpCount EC
    JOIN SumDepSalary DC ON EC.department_id = DC.department_id;
-- 5. Write a CTE that lists departments with more than 2 employees, then JOIN it with the departments table to also show department location.
WITH DepMoreThan2 AS (
    SELECT department_id,
        COUNT(*)
    FROM employees
    GROUP BY department_id
    HAVING COUNT(*) > 2
)
SELECT d2.*,
    d.location
FROM DepMoreThan2 d2
    INNER JOIN departments d ON d2.department_id = d.department_id;
-- 6.Write a CTE to find the top 2 highest earners overall (across all departments combined), then display their department names as well.
WITH HighestPayEmp AS (
    SELECT emp_id,
        salary,
        department_id
    FROM employees
    ORDER BY salary DESC
    LIMIT 2
)
SELECT HPE.emp_id,
    HPE.salary,
    HPE.department_id,
    D.dep_name
FROM HighestPayEmp HPE
    INNER JOIN departments D ON HPE.department_id = D.department_id
ORDER BY department_id;
