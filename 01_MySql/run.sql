SELECT * FROM employees;

SELECT d.dep_name, COUNT(e.first_name) AS employee_count
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
GROUP BY d.dep_name;