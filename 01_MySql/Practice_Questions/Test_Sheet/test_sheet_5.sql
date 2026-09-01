-- JOIN employees + departments, GROUP BY department, HAVING avg salary > 35000, ORDER BY total salary DESC.
SELECT d.department_id,
    d.dep_name,
    ROUND(AVG(e.salary), 2) AS average_salary,
    SUM(e.salary) AS total_salary
FROM employees e
    INNER JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_id,
    d.dep_name
HAVING AVG(e.salary) > 35000
ORDER BY total_salary DESC;
-- Find departments where the employee count is above average department employee count (this needs a subquery + GROUP BY together — attempt it, it's meant to stretch you).
SELECT d.dep_name,
    COUNT(e.emp_id) AS emp_count
FROM employees e
    INNER JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_id,
    d.dep_name
HAVING COUNT(e.emp_id) > (
        -- Subquery jo average employee count nikalegi
        SELECT AVG(department_count)
        FROM (
                SELECT COUNT(emp_id) AS department_count
                FROM employees
                GROUP BY department_id
            ) AS subquery
    );
-- Full report: department name, employee count, total salary, average salary — one single query, sorted by total salary descending.
SELECT d.dep_name,
    COUNT(e.emp_id) AS emp_count,
    SUM(e.salary) AS total_salary,
    AVG(e.salary) AS average_salary
FROM employees e
    INNER JOIN Departments d ON e.department_id = d.department_id
GROUP BY d.dep_name
ORDER BY total_salary DESC;