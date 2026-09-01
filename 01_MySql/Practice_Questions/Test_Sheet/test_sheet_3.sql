-- INNER JOIN employees and departments — show employee name + department name.
SELECT e.emp_id,
    CONCAT(e.first_name, ' ', e.last_name) AS Emp_Name,
    d.department_id,
    d.dep_name
FROM employees e
    INNER JOIN departments d ON e.department_id = d.department_id;
-- LEFT JOIN — show ALL employees even if their department doesn't exist in departments.
SELECT e.*,
    d.*
FROM employees e
    LEFT JOIN departments d ON e.department_id = d.department_id;
-- Find departments that have NO employees (use LEFT JOIN + WHERE IS NULL).
SELECT e.*,
    d.*
FROM employees e
    LEFT JOIN departments d ON e.department_id = d.department_id
WHERE e.department_id IS NULL;
-- SELF JOIN — find pairs of employees in the same department.
SELECT e.emp_id,
    concat(e.first_name, ' ', e.last_name) AS Emp_Name,
    ed.department_id,
    ed.hire_date
FROM employees e
    LEFT JOIN employees ed ON e.department_id = ed.department_id;
-- JOIN employees, departments, and projects together — show employee name, department name, and project name (3-table join).
SELECT concat(e.first_name, ' ', e.last_name) AS Emp_Name,
    d.department_id,
    p.project_name
FROM employees e
    INNER JOIN departments d ON e.department_id = d.department_id
    LEFT JOIN projects p ON d.department_id = p.department_id;